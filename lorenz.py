import numpy as np
from dataclasses import dataclass

@dataclass
class LorenzParams:
    tau_0: float = 50
    delta_tau: float = 20
    
    sigma: float = 10
    r: int = 28
    b: float = 8 / 3

    is_modified = False


def generate_initial_val(rng, size=3):
    return rng.uniform(size=size)


def lorenz(t, unit_vec, p):
    x, y, z = unit_vec
    
    x_dot = p.sigma * (y - x)
    y_dot = x * (p.r - z) - y
    z_dot = x * y - p.b * z

    return np.array([x_dot, y_dot, z_dot])
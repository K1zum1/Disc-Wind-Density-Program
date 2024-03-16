import numpy as np
from astro_constants import AU


def coordinate_system():
    x_values = np.linspace(0.1, 64, 65)
    y_values = np.linspace(0.1, 64, 65)
    R_values = np.sqrt(np.add.outer(x_values**2, y_values**2))
    R_values *= AU
    return R_values, y_values 

R_values, y_values = coordinate_system()

def get_source_point(y_values):
    d = -5*AU
    D = y_values + d
    return D


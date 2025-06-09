import numpy as np
import numba

@numba.vectorize(['float32(float32, float32)'], target='cuda')
def gpu_offset_calculation(x, y):
    # GPU-accelerated offset calculation
    return (x**2 + y**2)**0.5
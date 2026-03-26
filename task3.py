import numpy as np
from numpy.random.mtrand import exponential

values = np.array([2, 4, 6, 8, 10])

square_root = np.sqrt(values)

exponential = np.exp(values)

logaritmic = np.log(values)

total_sum = np.sum(values)

cumulative_sum = np.cumsum(values)

print(f"square_root: {square_root}")
print(f"exponential: {exponential}")
print(f"logaritmic: {logaritmic}")
print(f"total_sum: {total_sum}")
print(f"cumulative_sum: {cumulative_sum}")
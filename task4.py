import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_sum = np.sum(data, axis=1)
col_sum = np.sum(data, axis=0)

min_val = np.min(data)
max_val = np.max(data)
mean_val = np.mean(data)

print(f"Row-wise Sum:    {row_sum}")
print(f"Column-wise Sum: {col_sum}")
print(f"Minimum Value:   {min_val}")
print(f"Maximum Value:   {max_val}")
print(f"Overall Mean:    {mean_val}")
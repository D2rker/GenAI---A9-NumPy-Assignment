import numpy as np

array_1d = np.arange(1,11)
array_2d = np.arange(1, 10).reshape(3,3)

list_array = np.array([10, 20, 30, 40, 50])
array = [("1D araay", array_1d), ("2D array", array_2d), ("list-based Array", list_array)]

for name, arr in array:
    print(f"{name}:")
    print(arr)
    print(f"shape: {arr.shape}")
    print(f"datatype: {arr.dtype}")
    print("-" * 25)


## astype - typecast the existing data-type of elements to desired ones
import numpy as np

arr = np.array([1.2, 2.5, 3.8])
arr_int = arr.astype(int)

print(arr_int)
print(arr_int.dtype)
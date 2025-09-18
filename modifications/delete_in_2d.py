## np.delete(array, row or column, axis = 0 or 1)

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr)

new_arr = np.delete(arr, 0, axis=1)
print(new_arr)
## ndim - returns the dimensions of the array
import numpy as np

arr_1d = np.array([1,2,3])
print(arr_1d.ndim)

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ndim)

arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr_3d.ndim)
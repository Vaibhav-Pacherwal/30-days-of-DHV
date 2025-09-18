## .concatenate((arr1, arr2), axis) - use to merge to distinct arrays
## axis 0 - vertical stacking
## axis 1 - horizontal stacking

import numpy as np

arr1 = np.array([1,3,5,6])
arr2 = np.array([2,4,5,6])

merged_arr = np.concatenate((arr1,arr2))
print(merged_arr)

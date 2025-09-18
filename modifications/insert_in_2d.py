## .insert(arr, index, value, axis)
## axis = 0 & 1 for row & column insertion respectively

import numpy as np

arr = np.array([[10,20,20],
                [40,50,60],
                [70,80,90]])

new_arr_row = np.insert(arr, 1, [100,110,120], axis=0)
print(new_arr_row)

new_arr_col = np.insert(arr, 1, [100,110,120], axis=1)
print(new_arr_col)
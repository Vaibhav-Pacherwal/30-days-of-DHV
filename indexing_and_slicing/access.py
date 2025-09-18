import numpy as np

arr_1d = np.array([10,20,30,40,50])
print(arr_1d[0])
print(arr_1d[1:len(arr_1d)-2])
print(arr_1d[::2])

reversed_arr_1d = arr_1d[::-1]
print(reversed_arr_1d)
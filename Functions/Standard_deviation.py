import numpy as np
import time

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Computed by numpy: " + str(np.std(arr)))

sta = end = time.time() * 10E10
def std_noUseNumpy(arr):
    if len(arr)==0 or len(arr)==1:
        return 0;
    x_bar, s = sum(arr)/len(arr), 0
    arr_new = (arr - x_bar) ** 2
    return (sum(arr_new) / len(arr)) ** 0.5


end = time.time() * 10E10
print("Computer by original python: " + str(std_noUseNumpy(arr)) + ". Time taken: " + str(end-sta))

sta = end = time.time() * 10E10
def std_forLoop(arr):
    l = len(arr)
    if l==0 or l==1:
        return 0
    s = arr[0]
    for i in range(1, l):
        s += arr[i]
    avg = s/l
    s = (arr[0] - avg) ** 2
    for i in range(1, l):
        s += (arr[i] - avg) ** 2
    return (s/l) ** 0.5


end = time.time() * 10E10
print("Computed by for loop:        " + str(std_forLoop(arr)) + ". Time taken: " + str(end-sta))
    


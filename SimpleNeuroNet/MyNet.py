import numpy as np

import tensorflow as tf

def merge(arr1, arr2):
    i=0
    j=0
    k=0
    arr3 = np.empty(len(arr1)+len(arr2))
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i+=1
        elif arr2[j] < arr1[i]:
            arr3[k] = arr2[j]
            j+=1

        elif arr2[j] == arr1[i]:
            arr3[k] = arr1[i]
            k+=1
            arr3[k] = arr1[j]
            j +=1
            i +=1

        k+=1
    print(k)
    print(i , j)
    while i < len(arr1):
        print("I")
        arr3[k] = arr1[i]
        k+=1

    while j < len(arr2):
        arr3[k] = arr2[j]
        j+=1
        k+=1

    return arr3
######################################################################
def main():
    arr1 = [1,4,8,12,44,55,66,77]
    arr2 = [2,3,5,6,99,0,65,32]
    arr3 = merge(arr1, arr2)
    print(arr3)

main()
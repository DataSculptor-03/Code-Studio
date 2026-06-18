import sys

def findUnique(arr, n) :
    #write your code here 
    pass
    ele=-1
    for i in arr:
        if arr.count(i)==1:
            ele=i
            break
    return ele

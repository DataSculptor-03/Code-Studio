def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    pass
    count=0
    l=[]
    for row in mat:
        for i in row:
            l.append(i)
    if target in l:
        count=1
    else:
        count=0
    return count==1

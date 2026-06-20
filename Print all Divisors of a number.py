from typing import List

def printDivisors(n: int) -> List[int]:
    # Write your code here
    pass
    l=[]
    for i in range(1,(n//2)+1):
        if n%i==0:
            l.append(i)
    l.append(n)
    return l

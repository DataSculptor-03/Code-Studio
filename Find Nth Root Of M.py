def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    pass
    cal = round(m ** (1/n))  
    if cal ** n == m:
        return cal
    else:
        return -1

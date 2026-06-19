def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    pass
    mi=min(a)
    ma=max(a)
    s=set(a)
    l=list(s)
    l.remove(mi)
    l.remove(ma)
    l.sort()
    return [l[len(l)-1], l[0]]

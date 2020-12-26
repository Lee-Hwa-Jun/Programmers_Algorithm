def solution(n, lost, reserve):
    lost_clone = list(lost)
    for x in lost_clone:
        if x in reserve:
            lost.remove(x)
            reserve.remove(x)
    lost_clone=list(lost)
    for x in lost_clone:
        if x-1 in reserve:
            lost.remove(x)
            reserve.remove(x-1)
        elif x+1 in reserve:
            lost.remove(x)
            reserve.remove(x+1)

    return n-len(lost)
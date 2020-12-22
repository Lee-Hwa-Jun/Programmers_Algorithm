def solution(a):
    res = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            res.append(a[i] + a[j])
    res = list(set(res))
    return sorted(res)
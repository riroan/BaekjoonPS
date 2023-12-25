def solution(arr):
    a = 1
    if len(arr) >= 11:
        return sum(arr)
    else:
        for i in arr:
            a *=i
        return a
def solution(a, b):
    aa = int(str(a) + str(b))
    bb = int(str(b) + str(a))
    return max(aa,bb)
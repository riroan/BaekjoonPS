from itertools import permutations
try:
    while 1:
        a,b=input().split()
        b=int(b)
        a=list(a)
        arr = []
        for i in permutations(a):
            arr.append(''.join(i))
        a = ''.join(a)
        if b >len(arr):
            print(f"{a} {b} = No permutation")
        else:
            print(f"{a} {b} = {arr[b-1]}")
except:
    pass
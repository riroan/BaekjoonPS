from itertools import permutations
for test in range(int(input())):
    print(f"#{test+1}", end=" ")
    n=int(input())
    arr = list(str(n))
    ok = False
    for i in permutations(arr):
        tmp = int(''.join(i))
        if tmp == n:
            continue
        if tmp%n == 0:
            ok = True
    if ok:
        print("possible")
    else:
        print("impossible")
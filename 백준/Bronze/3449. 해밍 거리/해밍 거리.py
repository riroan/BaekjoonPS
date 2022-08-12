import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    arr=list(map(int, list(input())))
    brr=list(map(int, list(input())))
    ans = 0
    for i, j in zip(arr, brr):
        if i!= j:
            ans+=1
    print(f"Hamming distance is {ans}.")
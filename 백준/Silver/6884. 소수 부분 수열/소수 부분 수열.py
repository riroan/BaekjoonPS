import sys
def input(): return sys.stdin.readline().strip()


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for test in range(int(input())):
    arr = list(map(int, input().split()))[1:]
    p = [0]
    for i in arr:
        p.append(p[-1]+i)
    n = len(arr)
    ok = False
    for i in range(2, len(arr)+1):
        flag = 0
        for k in range(i,n+1):
            t = p[k]-p[k-i]
            if isPrime(t):
                flag = 1
                print(f"Shortest primed subsequence is length {i}: ",end="")
                print(*arr[k-i:k])
                break
        ok|=flag
        if flag:
            break
    if not ok:
        print("This sequence is anti-primed.")

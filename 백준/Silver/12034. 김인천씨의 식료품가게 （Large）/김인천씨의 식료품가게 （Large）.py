import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    arr.sort()
    arr = [[i, 0] for i in arr]
    ans = []
    for i in range(2*n-1,-1,-1):
        if arr[i][1] == 0:
            t = arr[i][0]*3//4
            ans.append(t)
            arr[i][1] = 1
            for j in range(2*n-1,-1,-1):
                if arr[j][0] == t and arr[j][1]==0:
                    arr[j][1] = 1
                    break
    ans.reverse()
    print(f"Case #{test+1}:", *ans)
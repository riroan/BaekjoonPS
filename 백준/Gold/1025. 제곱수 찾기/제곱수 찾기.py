n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for i in range(n)]


def check(x, y):
    return 0 <= x < n and 0 <= y < m

ans = -1
for x in range(n):
    for y in range(m):
        for i in range(-9, 10):
            for j in range(-9, 10):
                s = ''
                k=0
                if i==0 and j==0:
                    continue
                while check(x+k*i,y+k*j):
                    s+=str(arr[x+k*i][y+k*j])
                    k+=1
                    if (int(int(s)**0.5))**2 == int(s):
                        ans = max(ans, int(s))
print(ans)

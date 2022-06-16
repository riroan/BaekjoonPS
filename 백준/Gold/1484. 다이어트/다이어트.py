g = int(input())
ans = []
for i in range(1, int(g**0.5)+1):
    if g % i == 0:
        a, b = i, g//i
        if a ==b:
            continue
        if a % 2 != b % 2:
            continue
        x = (a+b)//2
        y = (a-b)//2
        ans.append(max(abs(x),abs(y)))
if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
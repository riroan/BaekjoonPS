import sys
input = lambda: sys.stdin.readline().strip()

ans = 0
for test in range(int(input())):
    s = input()
    ans += "OI" in s or "01" in s
print(ans)

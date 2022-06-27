a = [1,2,3]
for i in range(60000):
    a.append((a[-1]+a[-2]+a[-3])%(10**9+9))
for _ in range(int(input())):
    print(a[int(input())//2])
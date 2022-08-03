n=int(input())
d = {}
for i in range(n):
    a,b=input().split()
    d[b] = a
s = input()
ss = ''
for i in s:
    ss+=d[i]
l,r = map(int, input().split())
print(ss[l-1:r])
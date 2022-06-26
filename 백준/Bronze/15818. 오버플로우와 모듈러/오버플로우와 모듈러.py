n,m=map(int ,input().split())
r = 1
for i in list(map(int, input().split())):
    r*=i
    r%=m
print(r)
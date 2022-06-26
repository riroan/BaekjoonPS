n=int(input())
arr = list(map(int, input().split()))
s= [0]*80002
for i in range(1, 80002):
    if i%3==0 or i%7==0:
        s[i] = i
ps = [0]
for i in s:
    ps.append(ps[-1]+i)
for i in arr:
    print(ps[i+1])
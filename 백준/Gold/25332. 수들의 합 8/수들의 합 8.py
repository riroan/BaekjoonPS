from collections import defaultdict
n=int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
pa=[0]
pb = [0]
d=defaultdict(int)
d[0] = 1
ans = 0
for i in range(n):
    pa.append(pa[-1]+arr[i])
    pb.append(pb[-1]+brr[i])
    ans+=d[pb[-1]-pa[-1]]
    d[pb[-1]-pa[-1]]+=1
print(ans)
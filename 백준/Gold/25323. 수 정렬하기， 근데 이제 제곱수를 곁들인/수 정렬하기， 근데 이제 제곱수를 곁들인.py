import math
n=input();a=list(map(int,input().split()))
for i,j in zip(a,sorted(a)):
  if math.isqrt(i*j)**2!=i*j:print("NO");break
else:print("YES")
import math;u=input
for _ in range(int(u())):a,b=u().split();print(sum([i==b for i in str(math.factorial(int(a)))]))
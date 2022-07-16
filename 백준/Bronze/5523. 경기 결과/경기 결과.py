ca,cb = 0,0
for _ in range(int(input())):
    a,b=map(int, input().split())
    if a> b:
        ca+=1
    elif a<b:
        cb+=1
print(ca,cb)
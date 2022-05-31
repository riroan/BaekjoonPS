ix = 0
m = 0
a,b=input().split()
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] == b[i+j]:
            cnt+=1
    if cnt > m:
        ix = i
        m = cnt
print(len(a)-m)
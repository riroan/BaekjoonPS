a,b=input().split()
if len(a)!=len(b):
    print(0)
else:
    cnt = 0
    for i,j in zip(a,b):
        if i == j:
            if i == '8':
                cnt+=1
        else:
            break
    print(cnt)
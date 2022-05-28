def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a,b=input().split()
ok = prime(int(a))
a = int(b+a)
ok &= prime(a)
if ok:
    print("Yes")
else:
    print("No")
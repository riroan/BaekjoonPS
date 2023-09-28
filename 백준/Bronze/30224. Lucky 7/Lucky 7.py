n=int(input())
s = str(n)
if '7' not in s and n%7:
    print(0)
elif n%7==0 and '7' in s:
    print(3)
elif n%7==0:
    print(1)
elif '7' in s:
    print(2)

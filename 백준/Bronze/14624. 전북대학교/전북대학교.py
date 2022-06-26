n=int(input())
if n&1:
    print('*'*n)
    print(' '*((n-1)//2),end="")
    print('*')
    for i in range((n+1)//2-1):
        print(' '*((n+1)//2-2-i), end="")
        print('*',end="")
        print(' '*(2*i+1), end="")
        print('*')
else:
    print("I LOVE CBNU")
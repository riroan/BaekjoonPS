def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


s = input()
a = int(s)
b = s[::-1]
if '3' in s or '4' in s or '7' in s:
    print("no")
else:
    bb = ''
    for i in b:
        if i == '6':
            bb += '9'
        elif i == '9':
            bb += '6'
        else:
            bb += i
    bb = int(bb)
    if isPrime(a) and isPrime(bb):
        print("yes")
    else:
        print("no")

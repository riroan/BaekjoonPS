# author:  riroan
# created:  2024.03.07 00:31:29
import sys
def input(): return sys.stdin.readline().strip()


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def get(a, b, c):
    arr = [a]
    if c > 0:
        while arr[-1] + c < b:
            arr.append(arr[-1] + c)
    else:
        while arr[-1] + c > b:
            arr.append(arr[-1] + c)
    return arr


n = int(input())
if n < 10 or isPrime(n-1):
    print("NO")
    exit(0)
print("YES")
match n % 6:
    case 0 | 2 | 4:
        ans = get(n % 4+2, n+1, 4) + get((n+2) %
                                         4+2, n+1, 4) + get(1, n+1, 4) + get(3, n+1, 4)
    case 1:
        ans = get((n+1) % 4+2, n-1, 4) + get((n-1) % 4+2, n-1, 4) + \
            [1] + get(n-2, 1, -4) + get(n-4, 1, -4) + [n, n-1]
    case 3:
        ans = get(10, n-5, 4) + get(4, n-5, 4) + \
            [2, n-5, 1] + get(n-2, 1, -4) + get(n-4, 1, -4)+[n, n-1, 6, n-3]
    case 5:
        ans = get((n-1) % 4+2, n+1, 4) + get((n+1) %
                                             4+2, n+1, 4) + get(1, n+1, 4) + get(3, n+1, 4)
print(*ans)

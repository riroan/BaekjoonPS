for i in range(int(input())):
    n = int(input())
    r = 1
    for i in range(1, n + 1):
        r *= i
        while r % 10 == 0:
            r //= 10
        r %= 10000000
    print(r % 10)

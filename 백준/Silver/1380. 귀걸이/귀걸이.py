test = 1
while True:
    n = int(input())
    if n == 0:
        break
    name = [input() for i in range(n)]
    cnt = ['' for i in range(n)]
    for i in range(n*2-1):
        a, b = input().split()
        cnt[int(a)-1] += b
    for i in range(n):
        if cnt[i] != 'AB' and cnt[i] != 'BA':
            print(test, name[i])
    test+=1
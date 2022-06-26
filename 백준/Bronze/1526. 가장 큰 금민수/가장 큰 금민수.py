arr = []
for i in range(1000000):
    s = str(i).replace('7','').replace('4','')
    if s == '':
        arr.append(i)
n = int(input())
for i in arr[::-1]:
    if i<=n:
        print(i)
        break
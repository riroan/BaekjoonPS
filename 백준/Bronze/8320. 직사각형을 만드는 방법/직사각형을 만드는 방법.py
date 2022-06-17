n = int(input())
arr = [0]*10000
arr[0] = 1
for j in range(1, 10000):
    s = set()
    for i in range(1, j+1):
        if (j+1) % i == 0:
            s.add((min(i, (j+1)//i), max(i, (j+1)//i)))
    arr[j] = arr[j-1]+len(s)
print(arr[n-1])

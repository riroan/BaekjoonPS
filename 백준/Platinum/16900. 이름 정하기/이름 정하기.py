arr = input().split()
b = arr[0]
k=int(arr[1])
lb = len(b)
fail = [0]*lb
j = 0
for i in range(1, lb):
    while j > 0 and b[i] != b[j]:
        j = fail[j-1]
    if b[i] == b[j]:
        j += 1
        fail[i] = j
l = len(b)
print(l*k-fail[-1]*(k-1))
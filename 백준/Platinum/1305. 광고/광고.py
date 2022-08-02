
n=int(input())
b=input()
lb = len(b)
fail = [0]*lb
j = 0
for i in range(1, lb):
    while j > 0 and b[i] != b[j]:
        j = fail[j-1]
    if b[i] == b[j]:
        j += 1
        fail[i] = j
print(n-fail[-1])
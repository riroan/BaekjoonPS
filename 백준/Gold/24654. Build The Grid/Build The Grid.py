n = int(input())
arr = [['W' for i in range(501)] for i in range(501)]
for i in range(0, 501, 2):
    for j in range(2*(i//2)+1):
        arr[i][j] = 'B'
for j in range(0, 501, 2):
    for i in range(2*(j//2)+1):
        arr[i][j] = 'B'
print('W'*n)
for i in arr[:n-1]:
    print(''.join(list(map(str, i[:n]))))
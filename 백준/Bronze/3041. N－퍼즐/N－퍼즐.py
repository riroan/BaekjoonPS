arr = [list(input()) for i in range(4)]
answer = [list('ABCD'),list('EFGH'), list('IJKL'), list('MNO.')]
ans = 0
for i in range(4):
    for j in range(4):
        if i+j == 6:
            break
        for k in range(4):
            for l in range(4):
                if answer[i][j] == arr[k][l]:
                    ans += abs(i-k)+abs(j-l)
print(ans)
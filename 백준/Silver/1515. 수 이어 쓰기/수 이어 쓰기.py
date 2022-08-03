arr = [str(i) for i in range(1, 30001)]
ix = 0
s = input()
i=0
j=0
while ix < len(s):
    ok = False
    while i < 30000:
        while j < len(arr[i]):
            if arr[i][j] == s[ix]:
                ok = True
                ix+=1
                # print(i,j)
                break
            j+=1
        if ok:
            break
        i+=1
        j=0
    if ix == len(s):
        # print(i,j)
        break
    # ix+=1
    j+=1
    if j == len(arr[i]):
        i+=1
        j=0
print(i+1)
a = input()
b = input()
i = 0
cnt = 0
while i < len(a)-len(b)+1:
    if a[i] == b[0]:
        ok = True
        for j in range(len(b)):
            if a[i+j] != b[j]:
                ok = False
                break
        if ok:
            cnt += 1
            i += len(b)-1
    i += 1
print(cnt)

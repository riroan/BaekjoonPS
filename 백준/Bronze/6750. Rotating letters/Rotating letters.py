s=input()
ok = 1
for i in s:
    if i not in "IOSHZXN":
        ok = 0
if ok:
    print("YES")
else:
    print("NO")
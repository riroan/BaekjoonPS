a = list(map(int, list(input())))
b = list(map(int, list(input())))
ans1 = ''
ans2 = ''
ans3 = ''
ans4 = ''
ans5 = ''
for i, j in zip(a, b):
    if i and j:
        ans1+='1'
    else:
        ans1+='0'
    if i or j:
        ans2+='1'
    else:
        ans2+='0'
    if i^j:
        ans3+='1'
    else:
        ans3+='0'
    ans4 += str(1-i)
    ans5 += str(1-j)
print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
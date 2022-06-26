arr = input().split()
n = {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}

for ix, i in enumerate(arr):
    if i in n and ix:
        continue
    print(i[0].capitalize(), end="")
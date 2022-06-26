arr = [1, 2, 3, 4, 5, 6, 9, 12, 16, 20, 27, 36,
       48, 64, 81, 108, 144, 192]
for i in range(90):
    arr.append(arr[-5]*4)
print(arr[int(input())-1])
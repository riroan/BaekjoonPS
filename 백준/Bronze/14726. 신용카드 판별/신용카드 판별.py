for i in range(int(input())):
    arr = list(map(int, list(input())))
    arr = [arr[i]*2 if i & 1==0 else arr[i] for i in range(16)]
    arr=  [arr[i]%10 + arr[i]//10 for i in range(16)]
    if sum(arr)%10:
        print("F")
    else:
        print("T")
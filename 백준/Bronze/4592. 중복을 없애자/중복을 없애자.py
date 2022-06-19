while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = arr[0]
    arr = arr[1:]
    i = 0
    s = 0
    while i < n:
        if arr[i] != arr[s]:
            print(arr[s], end = " ")
            s = i
        i+=1
    print(arr[s], end=" ")
    print("$")
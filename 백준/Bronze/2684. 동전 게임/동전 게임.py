for test in range(int(input())):
    s = input()
    arr = [0]*8
    for i in range(len(s)-2):
        t = 0
        for j in range(3):
            if s[i+j] == 'H':
                t|=(1<<(2-j))
        # print(s[i:i+3], t)
        arr[t]+=1
    print(*arr)
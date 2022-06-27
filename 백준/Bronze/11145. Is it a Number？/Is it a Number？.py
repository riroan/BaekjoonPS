for i in range(int(input())):
    try:
        n = int(input().strip())
        if n < 0:
            assert 0
        print(n)
    except:
        print("invalid input")
import sys
input = sys.stdin.readline

for test in range(int(input())):
    p1, p2 = 0,0
    arr = "RPS"
    for _ in range(int(input())):
        a,b = input().split()
        ok = False
        for j in range(3):
            if [a,b] == [arr[j], arr[(j+1)%3]]:
                ok = True
        if ok:
            p2+=1
            continue
        for j in range(3):
            if [a, b] == [arr[j], arr[(j-1) % 3]]:
                ok = True
        if ok:
            p1+=1
    if p1>p2:
        print("Player 1")
    elif p1<p2:
        print("Player 2")
    else:
        print("TIE")
while 1:
    a = list(input())
    b=list(input())
    if a == ['E'] and b ==['E']:
        break
    p1, p2=0,0
    for i,j in zip(a,b):
        if i == 'R' and j == 'S' or i == 'S' and j == 'P' or i == 'P' and j == 'R':
            p1+=1
        elif i != j:
            p2+=1
    print("P1:", p1)
    print("P2:", p2)

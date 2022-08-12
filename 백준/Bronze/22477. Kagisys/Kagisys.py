import sys
input = lambda: sys.stdin.readline().strip()

d = {}
t = 0
for test in range(int(input())):
    d[input()] = 0
for i in range(int(input())):
    s = input()
    try:
        d[s]
    except:
        print("Unknown", s)
        continue
    
    if t:
        print(f"Closed by", s)
        t = 0
    else:
        print(f"Opened by", s)
        t = 1
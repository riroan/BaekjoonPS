import re
p = re.compile('^[ABCDEF]?A+F+C+[ABCDEF]?$')
for test in range(int(input())):
    s = input()
    if p.match(s):
        print("Infected!")
    else:
        print("Good")
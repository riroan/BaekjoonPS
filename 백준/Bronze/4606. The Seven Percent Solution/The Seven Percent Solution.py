# author:  riroan
# created:  2024.03.27 20:33:08
import sys
def input(): return sys.stdin.readline().strip()


d = {" ": "%20", "!": "%21", "$": "%24",
     "%": "%25", "(": "%28", ")": "%29", "*": "%2a"}
dd = "% !$()*"
while 1:
    s = input()
    if s == '#':
        break
    for i in dd:
        s = s.replace(i, d[i])
    print(s)

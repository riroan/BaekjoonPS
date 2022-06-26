import sys
import string
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s = input().lower()
    arr = [0]*26
    for i in s:
        if i in string.ascii_lowercase:
            arr[ord(i)-ord('a')] = 1
    if sum(arr) == 26:
        print("pangram")
    else:
        print("missing ", end="")
        for i in range(26):
            if arr[i] == 0:
                print(chr(i+ord('a')),end="")
        print()
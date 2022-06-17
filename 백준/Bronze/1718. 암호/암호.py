s=input()
t=input()
arr = []
for i in range(len(s)):
    arr.append(ord(t[i%len(t)])-ord('a')+1)
    if s[i] == ' ':
        print(' ', end="")
    else:
        print(chr((ord(s[i])-ord('a')-(ord(t[i % len(t)])-ord('a')+1))%26+ord('a')),end = "")
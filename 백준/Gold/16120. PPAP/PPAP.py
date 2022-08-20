s=input()
ss = []
for i in s:
    ss.append(i)
    if len(ss)>=4:
        if ss[-4:] == list('PPAP'):
            ss.pop()
            ss.pop()
            ss.pop()
if ss == ['P']:
    print("PPAP")
else:
    print("NP")
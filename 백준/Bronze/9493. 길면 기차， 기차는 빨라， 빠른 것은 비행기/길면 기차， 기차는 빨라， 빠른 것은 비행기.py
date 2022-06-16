while True:
    a,b,c=map(int, input().split())
    if a+b+c==0:
        break
    t = round(abs(a*3600/b - a*3600/c))
    s = str(t%60)
    t//=60
    m = str(t%60)
    t//=60
    
    if len(m)<2:
        m='0'+m
    if len(s)<2:
        s='0'+s
    print(f"{t}:{m}:{s}")
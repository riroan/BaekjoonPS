while 1:
    s=float(input())
    if s == -1:
        break
    print("Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(s, s*0.167))
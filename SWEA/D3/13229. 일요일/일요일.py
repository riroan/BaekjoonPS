d = {"MON":6, "TUE":5, "WED":4, "THU":3, "FRI":2, "SAT":1, "SUN":7}

for test in range(int(input())):
    print(f"#{test+1}", end=" ")
    print(d[input()])
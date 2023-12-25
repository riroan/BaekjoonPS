def solution(num_list):
    s = ''
    ss = ''
    for i in num_list:
        if i%2:
            s += str(i)
        else:
            ss += str(i)
    return int(s)  + int(ss)
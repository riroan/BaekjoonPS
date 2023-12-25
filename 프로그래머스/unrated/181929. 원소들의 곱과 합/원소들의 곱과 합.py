def solution(num_list):
    a = 1
    b = sum(num_list)
    for i in num_list:
        a*=i
    return +(a < b**2)
    
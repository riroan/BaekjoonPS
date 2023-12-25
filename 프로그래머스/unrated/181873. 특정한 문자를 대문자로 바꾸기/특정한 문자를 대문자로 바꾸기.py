def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i in alp:
            answer += i.upper()
        else:
            answer+=i
    return answer
def solution(s):
    answer = True

    s_list = []

    for i in s:
        if i == '(':
            s_list.append(i)
        else:
            try:
                s_list.pop()
            except:
                return False

    if len(s_list) == 0:
        return True
    else:
        return False

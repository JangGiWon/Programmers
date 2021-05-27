def solution(left, right):
    answer = 0

    for v in range(left, right + 1):
        cnt = 0
        for c in range(1, v + 1):
            if v % c == 0:
                cnt = cnt + 1

        if cnt % 2 == 0:
            answer = answer + v
        else:
            answer = answer - v

    return answer

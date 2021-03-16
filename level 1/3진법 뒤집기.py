def solution(n):
    answer = ''

    while n >= 1:
        temp = n % 3
        n //= 3
        answer += str(temp)

    return int(answer, 3)

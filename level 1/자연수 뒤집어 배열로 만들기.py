def solution(n):
    answer = list(str(n))
    return list(map(int, reversed(str(n))))

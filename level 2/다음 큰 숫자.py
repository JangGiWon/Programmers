def solution(n):
    answer = 0
    n_bin = bin(n).count('1')

    for answer in range(n + 1, 1000001):
        if bin(answer).count('1') == n_bin:
            return answer

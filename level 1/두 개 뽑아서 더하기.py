def solution(numbers):
    answer = []

    for index, num in enumerate(numbers):
        for i, j in enumerate(numbers):
            if not index == i:
                temp = num + j
                if not temp in answer:
                    answer.append(temp)
    answer.sort()
    return answer
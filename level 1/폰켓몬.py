from collections import Counter


def solution(nums):
    answer = 0
    count = Counter(nums)

    if len(nums) / 2 <= len(count.keys()):
        answer = len(nums) / 2
    else:
        answer = len(count.keys())

    return answer

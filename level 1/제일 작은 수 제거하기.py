def solution(arr):
    answer = []
    min_value = min(arr)
    arr.remove(min_value)
    answer = arr
    return answer if answer != [] else [-1]

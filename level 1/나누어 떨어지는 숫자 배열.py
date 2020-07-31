def solution(arr, divisor):
    array = [x for x in arr if x % divisor == 0]
    array.sort()
    return array if len(array) else [-1]

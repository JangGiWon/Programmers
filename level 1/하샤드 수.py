# def solution(x):
#     return x % sum([int(n) for n in str(x)]) == 0

def solution(x):
    arr = list(str(x))
    sum = 0

    for i in arr:
        sum += int(i)

    return x % sum == 0

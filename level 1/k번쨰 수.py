def solution(array, commands):
    answer = []

    for key in commands:
        i, j, k = key[0], key[1], key[2]
        slice = array[i - 1 : j] 
        slice.sort()
        answer.append(slice[k - 1])

    return answer



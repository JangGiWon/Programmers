def solution(arr):
    answer = []
    for n in arr:
        if answer[-1:] == [n]: #[-1:]은 리스트 끝요소를 리스트 형태로 반환, 리스트가 비어있어도 오류 없음, 리스트를 반환하기에 리스트랑 비교해줘야함
            continue
        answer.append(n)
    return answer
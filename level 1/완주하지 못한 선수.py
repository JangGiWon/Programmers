import collections

'''
def solution(participant, completion):
    for people in completion:
        if people in participant:
            participant.remove(people)
        else:
            pass
    return participant[0]
'''
# 위처럼 풀면 시간 오래 걸림, 효울성 0
# collections 모듈을 사용해보자

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]
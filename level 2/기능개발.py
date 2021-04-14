def solution(progresses, speeds):
    answer = []
    count = 0
    days = 1

    for i in range(len(progresses)):
        if i == 0 and progresses[i] + speeds[i] * days >= 100:
            count += 1
            answer.append(count)
        elif i > 0 and progresses[i] + speeds[i] * days >= 100:
            count += 1
            answer[-1] += 1
        while progresses[i] + speeds[i] * days < 100:
            days += 1
            if progresses[i] + speeds[i] * days >= 100:
                count = 1
                answer.append(count)
                break

    return answer

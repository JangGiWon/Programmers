def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    match_cnt = 0
    zero_cnt = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:
            match_cnt += 1

    answer[0], answer[1] = rank[match_cnt + zero_cnt], rank[match_cnt]

    return answer

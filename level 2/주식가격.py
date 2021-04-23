def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            temp = stack.pop()
            answer[j] = i - temp
        stack.append(i)

    while stack:
        temp = stack.pop()
        answer[temp] = len(prices) - 1 - temp

    return answer

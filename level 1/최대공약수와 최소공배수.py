def solution(n, m):

    N = [i for i in range(1, n + 1) if n % i == 0]
    M = [i for i in range(1, m + 1) if m % i == 0]

    gcd = max([i for i in N if i in M])
    lcm = gcd * (n / gcd) * (m / gcd)

    answer = [gcd, lcm]
    return answer


print(solution(2, 10))

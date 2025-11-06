def digit_count(n):
    ans = 0
    while n > 0:
        n //= 10
        ans += 1
    return ans
def solution(num, i):
    ans = []
    while num > 0:
        pow = 10**i
        ans.append((num // pow)*pow)
        num %= pow
        i -= 1
    ans = [x for x in ans if x > 0]
    return ans
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a = int(input())
        no_of_digits = digit_count(a)
        ans = solution(a, no_of_digits)
        print(len(ans))
        print(' '.join(map(str, ans)))
# (1, 2,4,5) find missing number Hint : Sum of first n natural numbers

def sol(arr: list):
    n = len(arr) + 1
    n_sum = n * (n+1) // 2
    return n_sum - sum(arr)

print(sol([1,2,4,5]))
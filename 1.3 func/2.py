n, k = map(int, input().split())
def calc_c(n,k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return calc_c(n - 1, k) + calc_c(n - 1, k - 1)
print(calc_c(n, k))
def primes():
    i = 2
    while i <= i+1:
        summ = 0
        for j in range(1, i+1):
            if i % j == 0:
                summ += 1
        if summ == 2:
            yield i
        i += 1
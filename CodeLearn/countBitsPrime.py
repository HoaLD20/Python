def count_bits_prime(L, R):
    c = 0
    for i in range(L, R + 1):
        e = bin(i)
        a = e[2:]
        b = 0
        for j in range(len(a)):
            if a[j] == '1':
                b += 1
        if isPrime(b):
            c += 1
    return c


def isPrime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


print(count_bits_prime(1, 10))

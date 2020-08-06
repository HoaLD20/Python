while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        m = a // b
        n = a - m * b
        print(m, n, "/", b, end=" ")
        print()
    else:
        break

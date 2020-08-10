n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())

    m = (a + d) * (a + d) + b * b + c * c + 7 * (min(a + d, b, c))
    j = a * a + (b + d) * (b + d) + c * c + 7 * (min(a, b + d, c))
    k = a * a + b * b + (c + d) * (c + d) + 7 * (min(a, b, c + d))
    print(max(m, j, k))

n = int(input())
for i in range(n):
    x, y = map(float, input().split())
    print("{:.7}".format(60 * x / y - 60 * x / y / x), "{:.7}".format(60 * x / y),
          "{:.7}".format(60 * x / y + 60 * x / y / x))

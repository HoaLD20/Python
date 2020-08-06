n = float(input())
m = int(input())
count = 0
for i in range(m):
    a, b = map(float, input().split())
    count += a * b
print("{:.7f}".format(count*n))
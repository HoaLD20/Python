n = int(input())
num = []
count = 0
for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, y + 1):
        if i not in num:
            num.append(i)
            count += 1
    i += 1
print(count)

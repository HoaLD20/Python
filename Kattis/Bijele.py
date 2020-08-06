check = [1, 1, 2, 2, 2, 8]
# 0 1 2 2 2 7

num = list(map(int, input().split()))
for i in range(len(num)):
    print(check[i] - num[i], end=" ")


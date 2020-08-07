def check(k):
    for i in k:
        if i != 0:
            return False
    return True


n = int(input())
say = list(input().split())
say2 = []
for i in range(len(say)):
    j = i + 1
    if say[i].isdigit():
        say2.append(int(say[i]))
    else:
        say2.append(j)

m = list(range(1, n + 1))
k = list(map(int.__sub__, say2, m))

if not check(k):
    print("something is fishy")
else:
    print("makes sense")

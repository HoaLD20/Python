n = int(input())
data = {}
for i in range(n):
    a, b = input().split()
    try:
        if int(a):
            data.update({b: int(a) / 2})
        else:
            data.update({a: int(b)})
    except:
        None
for k, v in data.items():
    print(k, v)

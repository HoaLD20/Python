n = int(input())
data = {}
for i in range(n):
    a, b = input().split()
    try:
        if int(a):
            data.update({b: float(a)/2})
    except:
        data.update({a: int(b)})

# huhu = collections.OrderedDict(sorted(data.items()))
pro = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
for i in pro:
    print(i)

"""
6
16 red
9 blue
7 green
black 50
lala 120
test 190

"""
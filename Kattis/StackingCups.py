import collections
n = int(input())
data = {}
for i in range(n):
    a, b = input().split()
    try:
        if int(a):
            data.update({b: int(a)//2})
    except:
        data.update({a: int(b)})
huhu = collections.OrderedDict(sorted(data.items()))
for k, v in huhu.items():
    print(k)

"""
DONE
"""
a = list(map(int, input().split()))
n = a[0]  # chieu dai
h = a[1]  # khoang cach tu mep tren
v = a[2]  # khoang cach tu mep trai
k = n / 2  # 1/2 canh

if h < k:
    h = n - h
if v < k:
    v = n - v

print(h * v * 4)

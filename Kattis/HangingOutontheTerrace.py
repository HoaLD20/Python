a, b = map(int, input().split())  # a la so nguoi toi da, b la so luot ra vao
gr = 0  # so nhom nguoi khong duoc vao san thuong
peo = 0  # so nguoi dang o tren san thuong
n, h = input().split()
if "enter" in n:
    if int(h) <= a:
        peo += int(h)
    else:
        gr += 1
if "leave" in n:
    None
for i in range(b - 1):
    m, k = input().split()
    if "enter" in m:
        if int(k) + peo <= a:
            peo += int(k)
        else:
            gr += 1
    elif "leave" in m:
        if int(k) <= peo != 0:
            peo -= int(k)
print(gr)

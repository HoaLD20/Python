n = input()
t = 0
c = 0
g = 0
k = 0
for i in n:
    if i == "T":
        t += 1
    elif i == "C":
        c += 1
    elif i == "G":
        g += 1
meow = t * t + c * c + g * g
while t != 0 and c != 0 and g != 0:
    t -= 1
    c -= 1
    g -= 1
    k += 7
print(meow + k)

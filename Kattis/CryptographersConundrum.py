a = "PER"
b = input()
count = 0
for i in range(len(b)):
    if i %3 == 0:
        sub = b[i:i+3]
        for k in range(len(sub)):
            if sub[k] != a[k]:
                count += 1
        sub = ""

print(count)
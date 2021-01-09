value = input()
count = 0
a = b = ""
for i in range(len(value)):
    j = i
    while value[j] != "-":
        a += value[j]
        j += 1
    while value[j] != ";":
        b += value[j]
        j += 1



print(count)

"""
zepelepenapa papapripikapa

zelena paprika
"""

n = input()
n = list(n)
a = ["pa", "pe", "pi", "po", "pu"]
c = ["a", "e", "i", "o", "u"]
b = []

for i in range(len(n) - 2):
    if n[i] in c:
        j = i
        print(i)
        if n[j + 1] + n[j + 2] in a:
            n.remove(n[j + 1])
            n.remove(n[j + 1])
print("".join(b))

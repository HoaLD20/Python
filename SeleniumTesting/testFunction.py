import random
import string
import secrets


def phoneran():
    p = list('0000000000')
    p[0] = str(random.randint(1, 9))
    for i in [1, 2, 6, 7, 8]:
        p[i] = str(random.randint(0, 9))
    for i in [3, 4]:
        p[i] = str(random.randint(0, 8))
    if p[3] == p[4] == 0:
        p[5] = str(random.randint(1, 8))
    else:
        p[5] = str(random.randint(0, 8))
    n = range(10)
    if p[6] == p[7] == p[8]:
        n = (i for i in n if i != p[6])
    p[8] = str(random.choice(n))
    p = ''.join(p)
    return "09" + p[:1] + p[3:6] + p[6:]


def genaratePass():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    return password + "%" + "#" + "@"


print(phoneran())

a = input()  # get hands and value of suit
numOfPoint = int(a[0]) * 4  # number of input
number = ["A", "K", "Q", "J", "T", "9", "8", "7"]
dominant = [1, 4, 3, 20, 10, 14, 0, 0]
notdominant = [11, 4, 3, 2, 10, 0, 0, 0]
total = 0
while numOfPoint > 0:  # get input
    value = input()  # input
    getValue = value[0]  # get first value from input
    for i in range(len(number)):
        if getValue == number[i]:

            total += abs(dominant[i] - notdominant[i])

    numOfPoint -= 1

print(total)

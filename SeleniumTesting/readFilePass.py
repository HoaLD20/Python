
with open("pass.txt") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(len(content)-1):
        print("username:" + content[i])
        print("pass: "+content[i+1])
f.close()

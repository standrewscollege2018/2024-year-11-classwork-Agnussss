list = []
while True:
    name = input("enter a name: ")
    if name.lower() == "stop":
        break
    elif name.strip() == "":
        print("NO BLANKS MONKEY")
    else:
        list.append(name)
list.sort()
for i in range(len(list)):
    print(i+1, list[i])

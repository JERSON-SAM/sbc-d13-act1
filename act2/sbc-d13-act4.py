user = input("Enter something: ")
list = []
new = []
for i in user:
    if i.isalpha():
        list.append(i)
    
    elif i == " " or i == "," or i == ";" or i == ":" or i == "|":
        var = "".join(list)
        new.append(var)
        list.clear()

bago = "".join(list)
new.append(bago)
print(new)
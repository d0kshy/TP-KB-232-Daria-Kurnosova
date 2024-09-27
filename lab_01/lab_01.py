
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "surname":"Smith", "phone":"0631234567", "email":"bobsmith1234@gmail.com"},
    {"name":"Emma", "surname":"Thomas", "phone":"0631234567", "email":"emmathomas1234@gmail.com"},
    {"name":"Jon",  "surname":"Brown", "phone":"0631234567", "email":"jonbrown1234@gmail.com"},
    {"name":"Zak",  "surname":"Abrams", "phone":"0631234567", "email":"zakabrams1234@gmail.com"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    newItem = {"name": name, "surname":surname, "phone": phone, "email":email}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Deleted position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()
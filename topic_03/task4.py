def findInsPos(slist, nElem):
    for index, value in enumerate(slist):
        if nElem < value:
            slist.insert(index, nElem)
            return index
    slist.append(nElem)
    return len(slist)

newList = [1, 5, 3, 6, 9, 0]
print(f"\nList before modifications: {newList}.\n")

newList.sort()
print(f"List after sorting: {newList}.\n")

newElem = input("Enter the new element: ")
newElem = int(newElem)

findInsPos(newList, newElem)
print(f"\nList was updated: {newList}.")
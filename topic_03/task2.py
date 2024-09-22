
List = [1, 2, 4, 3, 7, 8]
print(f"\nList before: {List}.")

List.extend([5, 6])
print(f"List after extending: {List}.")

List = [1, 2, 4, 3, 7, 8]
List.append(5)
print(f"List after appending: {List}.")

List = [1, 2, 4, 3, 7, 8]
List.insert(5, 'a')
print(f"List after inserting: {List}.")

List = [1, 2, 4, 3, 7, 8]
List.remove(3)
print(f"List after removing: {List}.")

List = [1, 2, 4, 3, 7, 8]
List.clear()
print(f"List after clearing: {List}.")

List = [1, 2, 4, 3, 7, 8]
List.sort()
print(f"List after sorting: {List}.")

List = [1, 2, 4, 3, 7, 8]
List.reverse()
print(f"List after reversing: {List}.")

List = [1, 2, 4, 3, 7, 8]
newList = List.copy()
print(f"List after coping: {List}.\n   New list after coping: {List}")
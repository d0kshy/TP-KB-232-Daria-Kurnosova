dict = {'a': 1, 'b': 2}
print(f"\nDictionary before: {dict}.\n")

dict.update({'b': 3, 'c': 4})
print(f"Dictionary after updating a dictionary: {dict}.\n")

dict = {'a': 1, 'b': 2}
del dict['a']
print(f"Dictionary after deletin an element from the dictionary: {dict}.\n")

dict = {'a': 1, 'b': 2}
dict.clear()
print(f"Dictionary after clearing a dictionary: {dict}.\n")

dict = {'a': 1, 'b': 2}
keys = dict.keys()
print(f"Dictionary's keys: {keys}.\n") 

dict = {'a': 1, 'b': 2}
values = dict.values()
print(f"Dictionary's values: {values}.\n") 

dict = {'a': 1, 'b': 2}
items = dict.items()
print(f"Dictionary's items: {items}.\n")
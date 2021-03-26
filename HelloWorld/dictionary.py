# list of pairs, maps
d = {'name': "max", 'age': 14, 'year': 2004}
print(d)
# name is a key, max is a value
print(d['name'])
print(d['age'])
e = {'name': 'Tom', 15: 15, 15.1: 15.1, True: True, (2,3): 5}
# all values can be key and values
print(e[(2, 3)])
print(e[True])
print(len(e))
print(e.get('name'))
# add one pairs
e['Surname'] = "Tesar"
print(e)
e.pop('Surname')
print(e)
e.clear()
print(e)
e[1] = 1
print(e)
del e

# change existing value with a key
d['name'] = 'new name'
print(d)
d.update({'name': 'max'})
print(d)
print()
print("the keys are: ", d.keys())
print("the values are: ", d.values())
print("the items are: ", d.items())
# pop last item edited/added
print(d.popitem())
print(d)

diction = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x, y in diction.items():
    print(x,y, end=", ")

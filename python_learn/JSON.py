import json
import mymodule as mm

# string convert to a dic using JSON
x = '{"name":"John","age":30,"city":"Ner York"}'
print(type(x))
y = json.loads(x)
print(type(y))
print(y["age"])
print("*****",json.dumps(x,indent=4,sort_keys=True))

# person1 object convert to a string using JSON
a = json.dumps(mm.person1)
print(type(a))
# print(a)

person = {"name":"Emerald","age":18,"gender":"female"}
# json.dumps(person,indent=1)
print(json.dumps(person,indent=1))
print(json.dumps(person))
print(json.dumps(person,indent=4,sort_keys=True))


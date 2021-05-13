thisdict = {
    "name": "Emerald",
    "age": 18,
    "major": "cs"
}
print(thisdict["name"])
print(thisdict["age"])

key = thisdict.keys();
print(key)
value = thisdict.values();
print(value)

thisdict["age"]=19
print(thisdict)

print(thisdict.items())
thisdict.update({"name":"liu"})
thisdict["gender"] = "female"
thisdict.pop("gender")
thisdict.popitem()
# del thisdict["age"]
print(thisdict)

for x,y in thisdict.items():
    print("key=",x," value=",y)

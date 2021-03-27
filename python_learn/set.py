set1 = {1,2,3,5,4,4}
print(set1)
# set has no index, and order doesn't matter
set1.add(0)
print(set1)
set2 = {-1,-4,-10}
set1.update(set2)
print(set1)
set1.remove(-10)
print(set1)
set1.discard(-10)
print(set1)

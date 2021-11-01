myDict = {'name': 'Chichi-Gogo-Dany', 'age': 26}
print(myDict)
########Search for value in a dictionary#########
def searchDict(dict, value):
    for key in dict: #-------------> O(n)
        if dict[key] == value: #------> O(1)
            return key, value #--------> O(1)
    return 'THe value does not exist'

print(searchDict(myDict, 26))

#############Delete and element from a dictionary###
myDict = {'name': 'Chichi-Gogo-Dany', 'age': 26}
myDict.pop('age')
print(myDict.clear())

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)

my_dict = {}
my_dict[(1, 2, 4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)
print(my_dict)

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for k in arr:
    sum += arr[k]

print(sum)

a = {(1,2):1,(2,3):2}
print(a[1,2])

dict = {'c': 97, 'a': 96, 'b': 98}
for _ in sorted(dict):
    print (dict[_])

rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
print(id(r))
print(id(rec))
print(id(r) == id(rec))


init_tuple = ()
print (init_tuple.__len__())

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print(init_tuple_a == init_tuple_b)

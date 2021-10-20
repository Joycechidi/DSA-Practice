import numpy as np

twoArray = np.array([[11, 15, 10, 6], [10,14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoArray)

def traverse2DArray(twoArray):
    for i in range(len(twoArray)): #----------------> O(n)
        for j in range(len(twoArray[0])):#---------> O(m)
            print(twoArray[i][j])

traverse2DArray(twoArray)

#search2DArray - Linear search
import numpy as np

twoArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoArray)

def search2DArray(array, value):

    '''
    Search for an element in 2D array
    :param array:
    :param value:
    :return:
    '''

    for i in range(len(array)): #--------> O(n)
        for j in range(len(array[0])):  #-----> O(m)
            if array[i][j] == value:    #----->  O(1)
                return 'The value is located at index '+str(i)+" "+str(j)
    return 'The element is not found'
print(search2DArray(twoArray, 6))

#DELETING A ROW / COLUMN FROM 2D ARRAY

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

new2DArray = np.delete(twoDArray, 0, axis=1)  #-----> O(nm)
print(new2DArray)

a = [1, 2, 3, 4, 5]
print(a[3:0:-1])


arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end = " ")


#What will be the output of the following code block?

def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)

#What will be the output of the following code block?

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)

#What will be the output of the following code snippet?

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

#What will be the output of the following code block?

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
print(sum)

#What will be the output of the following code block?

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

#What will be the output of the following code block?

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v

#What is the correct command to shuffle the following list?

fruit=['apple', 'banana', 'papaya', 'cherry']
print(fun(data[0]))

def decimal2Binary(num):

    assert num == int(num), 'The number must be a positive number'
    if num == 0:
        return 0
    return num%2 + 10 * decimal2Binary(int(num/2))

print(decimal2Binary(13))


def productOfArray(arr):

    if len(arr) == 0:
        return 0
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1, 2, 4, 6]))


def recursiveRange(num):
    '''
    num = num + num-1 + num-2 + ... 1 + 0
    num + recursiveRange(num - 1)

    :param num:
    :return:
    '''

    assert int(num) ==  num, 'The parameter must be only an integer!'
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)

print(recursiveRange(12))
print(recursiveRange(6))
print(recursiveRange(10))


def fib(num):
    '''


    :param num:
    :return:
    '''
    assert int(num) == num, 'The number must be a positive integer!'
    if num in [0, 1]:
        return num
    return fib(num - 1) + fib(num - 2)
print(fib(4))
print(fib(10))
print(fib(28))
#print(fib(35))

def reverse(strng):
    '''
    Write a recursive function called reverse which accepts a string and returns a new string in reverse

    :param strng:
    :return:
    '''
    if len(strng) <= 1:
        return strng
    return strng[-1] + reverse(strng[:-1])
print(reverse('python'))
print(reverse('Joyce'))

def isPalindrome(strng):
    '''
    Write a recursive function called isPalindrome
    which returns true if the string passed to it is a
    palindrome (reads the same forward and backward).
    Otherwise it returns false.


    :param strng:
    :return:
    '''
    #Check for empty string
    if len(strng) <= 1:
        return True
    elif strng[0] != strng[-1]:
        return False
    else:
        return isPalindrome(strng[1: -1])

print(isPalindrome(" "))
print(isPalindrome("a"))
print(isPalindrome("awesome"))
print(isPalindrome("amanaplanacanalpandemonium"))
print(isPalindrome("amanaplanacanalpanama"))


def isOdd(num):
    '''
    Write a recursive function called "someRecursive" which
    accepts an array and a callback. The function return true if a
    single value in the array returns true when passed
    to the callback. Otherwise it returns false.
    :param num:
    :return:
    '''

    if num % 2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not cb(arr[0]):
        return someRecursive(arr[1:], cb)
    return True
print(someRecursive([1,2,3,4], isOdd))


def capitalizeFirst(arr):
    '''
    Write a recursive function called capitalizeFirst.
    Given an array of strings, capitalize the first letter of each string in the array

    :param arr:
    :return:
    '''
    capital = []
    if len(arr) == 0:
        return capital
    capital.append(arr[0][0].upper() + arr[0][1:])
    return capital + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car', 'cat', 'orange', 'tall']))

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum += obj[key]
    return sum
print(nestedEvenSum(obj = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}))

def flatten(arr):
    '''
    Write a recursive function called flatten which accepts an array of arrays
    and returns a new array with all values flattened
    :param arr:
    :return:
    '''
    flatArr = []

    for value in arr:
        if type(value) is list:
            flatArr.extend(flatten(value))
        else:
            flatArr.append(value)
    return flatArr

    return arr


def capitalizeWords(words):
    '''

    :param words:
    :return:
    '''
    capital = []
    if len(words) == 0:
        return capital
    capital.append(words[0].upper())
    return capital + capitalizeWords(words[1:])
print(capitalizeWords(['i', 'am']))

def stringifyNumbers(obj):
    '''
    Write a function called stringifyNumbers which takes in an
    object ad finds all of the values which are numbers and
    converts to strings.
    :param obj:
    :return:
    '''

    newObj = obj

    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] + stringifyNumbers(newObj[key])
    return newObj


def collectStrings(obj):
    # TODO
    '''
    Write a function called collectStrings which accepts
    an object and returns an array of all the values
    in the object that have a typeof string
    :param obj:
    :return:
    '''
    collect = []
    for value in obj:
        if type(obj[value]) is str:
            collect.append(obj[value])
        elif type(obj[value]) is dict:
            return collect + collectStrings(obj[value])
    return collect





# Question 1: Find the missing number in an integer array of 1 to 100
# Hint: 1 + 2 + 3 + ... + n = n(n + 1)/2
# Find missing by using sum of series equation?

myList = [1, 2, 3, 5, 6, 7, 8, 9, 10]


def find_missing_number(arr, n):
    sum1 = 10 * 11 / 2
    sum2 = sum(arr)

    print(sum2 - sum1)


find_missing_number(myList, 100)


# for i in range(1, 101):
#     if arr[i+1] != arr[i]+1:
#         return "A number is missing"
# return "There is no missing number"

# Question 2: Write a program to find all pairs/ Two Sum of integers whose sum is equal to a given number
# Ask these questions to the interviewer.
# - Does array contain only positive  or negative numbers?
# - What if the same pair repeats twice, should we print it every time?
# - Is the reverse of the pair acceptable? e.g. Can we print both (4, 1) and (1, 4) if the given number is 5?
# - Do we need to print only distinct pairs? Is (3, 3)a valid pair given sum of 6?
# How big is the array?


def find_all_pairs(arr, target_num):
    for i in range(len(arr)):
        first_num = arr[i]
        second_num = target_num - first_num
        if first_num == second_num:
            return "Same pairs not valid"
        elif first_num + second_num == target_num:
            return [first_num, second_num]
    return []


print(find_all_pairs([2, 2, 3, 1, 4, 6, 5, ], 4))

# Option 2
# def find_all_pairs(arr, target_num):
#
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j]:
#                 continue
#             elif arr[i] + arr[j] == target_num:
#                 print(i, j)
#     return
#
#
# print(find_all_pairs([2, 2, 3, 1, 4, 6, 5,], 4))


# Question 3: Check if an array contains a number
import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def find_number(array, num):
    for i in range(len(array)):
        if array[i] == num:
            print(str(i) + " is the index of the number we are looking for.")
        # return "Number does not exist"


find_number(myArray, 10)
find_number(myArray, -1)

# Question 4 - Find the maximum product of two integers in the array where all elements are positive
import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def max_product(arr):
    maxprod = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            product = arr[i] * arr[j]
            if product >= maxprod:
                maxprod = product
                pairs = str(arr[i]) + "," + str(arr[j])
        print(pairs)
        print(maxprod)


# Question 5: IS Unique or Contains Duplicates - Implement an algorithm to determine
# if a list has all unique characters, using python list

myList = [1, 20, 30, 4, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 21]


def is_unique(myList):
    seen = []
    for i in myList:
        if i in seen:
            print(i)
            return False
        else:
            seen.append(i)
    return True


print(is_unique(myList))


# Question 6: Permutation. Given two lists,
# write a method to determine if one is a permutations of each other
def permutation(list1, list2):
    # check length of lists

    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    return False


list1 = [1, 2, 3]
list2 = [3, 2, 1, 0]

print(permutation(list1, list2))


#Question 7: Rotate Matrix: Given an image represented by an NxN matrix,
#write a method to rotate the image by 90 degrees
# 1 2 3                 7 4 1
# 4 5 6 --------------> 8 5 2
# 7 8 9                 9 6 3
#Create a temp variable to store the top left element to give way for the rotation
import numpy as np
my_2D_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(my_2D_array)

def rotate_matrix_90(matrix):
    n = len(matrix)
    # m = len(matrix)[0]

    #n//2 will give us the number of layers in a matrix
    for layer in range(n//2):
        first = layer
        last = n - layer - 1

        #save top element
        for i in range(first, last):
            top = matrix[layer][i]
            #move left element to top
            matrix[layer][i] = matrix[-i -1][layer]
            # move bottom to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i -1]
            #move right to bottom
            matrix[-layer -1][-i -1] = matrix[i][-layer - 1]
            # move to right
            matrix[i][-layer -1] = top
    return matrix
print(rotate_matrix_90(my_2D_array))







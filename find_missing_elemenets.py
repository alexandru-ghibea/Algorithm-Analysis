# Find the Missing Element
# Problem
# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number


def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for index in range(len(arr1)):
        if arr2[index] != arr1[index]:
            return arr1[index]
            break

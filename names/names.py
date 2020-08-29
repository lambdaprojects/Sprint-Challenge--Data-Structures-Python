import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
binarySearchTree = BinarySearchTree(names_1[0])
for name in names_1:
    binarySearchTree.insert(name)

for name in names_2:
    if (binarySearchTree.contains(name)):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# I am going to try using binary search
# Sort the first array and loop the second array to find the duplicate

def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1

duplicates = []
start_time = time.time()
names_1.sort()
for name in names_2:
    if binary_search(names_1, name ) == 1:
        duplicates.append(name)
end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

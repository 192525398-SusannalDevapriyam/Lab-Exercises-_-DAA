"""1.
words = ["tree","racecar", "madam"]

for i in words:
    if i == i[::-1]:
        print(i)
        break
else:
    print("empty string")"""
#---------------------------------------------------------

"""2.
nums1 = [2, 3, 2]
nums2 = [1, 2]

answer1 = 0
answer2 = 0

for i in nums1:
    if i in nums2:
        answer1 += 1

for i in nums2:
    if i in nums1:
        answer2 += 1

print([answer1, answer2])"""
#---------------------------------------------------------

"""3.
nums=[1,2,1]
total = 0

for i in range(len(nums)):
    for j in range(i,len(nums)):
        sub=nums[i:j+1]
        count= len(set(sub))
        total+=count**2
print(total)"""

#---------------------------------------------------------
"""4.
nums =[1,2,3,4]
count=0
k=1

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j] and (i*j) % k ==0:
            count+= 1
print(count)"""

#---------------------------------------------------------
"""5.
nums = [-10, 2, 3, -4, 5]

maximum = nums[0]

for i in nums:
    if i > maximum:
        maximum = i

print(maximum)"""

#---------------------------------------------------------
"""6.
nums = [3, 1, 5, 2, 4]

if len(nums) == 0:
    print("List is empty")
else:
    nums.sort()
    print("Sorted List:", nums)
    print("Maximum Element:", nums[-1])"""

#---------------------------------------------------------

nums=[1,3,4,5,7,5,9,5,2,3,4]
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)

#----------------------------------------------------------
"""8.
arr = [5, 2, 8, 1, 3]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)"""

#----------------------------------------------------------
"""9.
arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = 10

arr.sort()
print("sorted array :",arr)

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element", key, "is found at position", mid + 1)
        found = True
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element", key, "is not found")"""

#------------------------------------------------------------
"""def countWays(m, n, N, i, j):

    if i < 0 or i >= m or j < 0 or j >= n:
        return 1

    if N == 0:
        return 0

    up = countWays(m, n, N-1, i-1, j)
    down = countWays(m, n, N-1, i+1, j)
    left = countWays(m, n, N-1, i, j-1)
    right = countWays(m, n, N-1, i, j+1)

    return up + down + left + right


m = 2
n = 2
N = 2
i = 0
j = 0

print(countWays(m, n, N, i, j))"""

input("Press Enter to exit...")

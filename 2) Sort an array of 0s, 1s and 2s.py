def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [0, 2, 1, 2, 0, 1]
n = 6
sortArray(arr)
for num in arr:
    print(num, end=" ")
print()

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Algorithm / Intuition
# This problem is a variation of the popular Dutch National flag algorithm.

# This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:

# 1) arr[0….low-1] contains 0. [Extreme left part]
# 2) arr[low….mid-1] contains 1.
# 3) arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array

# Approach:

# Note: Here in this tutorial we will work based on the value of the mid pointer.

# The steps will be the following:

# 1) First, we will run a loop that will continue until mid <= high.
# 2) There can be three different values of mid pointer i.e. arr[mid]
#    (i)   If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to(low-1) only contains 0.
#    (ii)  If arr[mid] == 1, we will just increment the mid pointer and then the index(mid-1) will point to 1 as it should according to the rules.
#    (iii) If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to(n-1) only contains 2.
#          In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
# 3) Finally, our array should be sorted.

# Time Complexity: O(N), where N = size of the given array.
# Space Complexity: O(1) as we are not using any extra space.

# Python program to check for the sum
# condition to be satisfied

def hasArrayTwoCandidates(A, n, sum):

    # sort the array
    A.sort()
    left = 0
    right = n-1

    # traverse the array for the two elements
    while left < right:
        if (A[left] + A[right] == sum):
            return 1
        elif (A[left] + A[right] < sum):
            left += 1
        else:
            right -= 1
    return 0


# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 16
if (hasArrayTwoCandidates(A, len(A), n)):
    print("Yes")
else:
    print("No")

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Optimized Approach(using two-pointer):

# Intuition: In this approach, we will first sort the array and will try to choose the numbers in a greedy way.

# The steps are the following:

# 1) We will sort the given array first.
# 2) Now, we will take two pointers i.e. left, which points to the first index, and right, which points to the last index.
# 3) Now using a loop we will check the sum of arr[left] and arr[right] until left < right.
#    (i)   If arr[left] + arr[right] > sum, we will decrement the right pointer.
#    (ii)  If arr[left] + arr[right] < sum, we will increment the left pointer.
#    (iii) If arr[left] + arr[right] == sum, we will return the result.
# 4) Finally, if no results are found we will return “No” or {-1, -1}.


# Time Complexity: O(N) + O(N*logN), where N = size of the array.
# Reason: The loop will run at most N times. And sorting the array will take N*logN time complexity.

# Space Complexity: O(1) as we are not using any extra space.

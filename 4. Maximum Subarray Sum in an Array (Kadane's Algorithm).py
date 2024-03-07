import sys


def MaxiSum(arr):
    maxi = -sys.maxsize-1
    sum = 0

    for i in range(len(arr)):
        sum = sum + arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0
    return maxi


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxsum = MaxiSum(arr)
print("The Maximum Subarray is..", maxsum)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Optimal Approach - Kadane's Algorithm
# Kadane’s Algorithm is a dynamic programming algorithm used to solve the maximum subarray problem.
# The maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array of numbers that has the largest sum.

# Intuition:
# The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0.
# A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.

# Approach:
# The steps are as follows:

# 1) We will run a loop(say i) to iterate the given array.
# 2) Now, while iterating we will add the elements to the sum variable and consider the maximum one.
# 3) If at any point the sum becomes negative we will set the sum to 0 as we are not going to consider it as a part of our answer.

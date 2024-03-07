def MajorityElement(arr):
    n = len(arr)  # size of an given array
    count = 0    # Count
    el = None    # Element

    # Applying the Algorithm
    for i in range(n):
        if count == 0:
            count = 1
            el = arr[i]
        elif el == arr[i]:
            count += 1
        else:
            count -= 1

    # Check if the stored element is majority element
    count1 = 0
    for i in range(n):
        if arr[i] == el:
            count1 += 1

    if count1 > (n/2):
        return el
    return -1


arr = [2, 2, 1, 1, 2, 2]
ans = MajorityElement(arr)
print("MajorityElement is", ans)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Optimal Approach: Moore’s Voting Algorithm:

# Approach:
# 1) Initialize 2 variables:
#    Count – for tracking the count of element
#    Element – for which element we are counting
# 2) Traverse through the given array.
#    (i)   If Count is 0 then store the current element of the array as Element.
#    (ii)  If the current element and Element are the same increase the Count by 1.
#    (iii) If they are different decrease the Count by 1.
# 3) The integer present in Element should be the result we are expecting

# Time Complexity: O(N) + O(N), where N = size of the given array.
# Reason: The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.
# Note: If the question states that the array must contain a majority element, in that case, we do not need the second check. Then the time complexity will boil down to O(N).

# Space Complexity: O(1) as we are not using any extra space.

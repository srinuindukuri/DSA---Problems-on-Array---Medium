def MajorityElement(arr):
    n = len(arr)
    count1, count2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')

    # applying the Extended Boyer Moore’s Voting Algorithm:
    for i in range(n):
        if count1 == 0 and el2 != arr[i]:
            count1 = 1
            el1 = arr[i]
        elif count2 == 0 and el1 != arr[i]:
            count2 = 1
            el2 = arr[i]
        elif arr[i] == el1:
            count1 += 1
        elif arr[i] == el2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    ls = []  # list of answers

    # Manually check if the stored elements in
    # el1 and el2 are the majority elements:

    for i in range(n):
        if arr[i] == el1:
            count1 += 1
        if arr[i] == el2:
            count2 += 1

    mini = int(n/3) + 1
    if count1 >= mini:
        ls.append(el1)
    if count2 >= mini:
        ls.append(el2)

    # Uncomment the following line
    # if it is told to sort the answer array:
    # ls.sort() #TC --> O(2*log2) ~ O(1);

    return ls


arr = [1, 1, 1, 1, 2, 2, 3, 3, 3]
ans = MajorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()


# Optimal Approach(Extended Boyer Moore’s Voting Algorithm):
# Approach:
# 1) Initialize 4 variables:
#    (i)  -  cnt1 & cnt2 – for tracking the counts of elements
#    (ii) -  el1 & el2 – for storing the majority of elements.
# 2) Traverse through the given array.
#    (i)   - If cnt1 is 0 and the current element is not el2 then store the current element of the array as el1 along with increasing the cnt1 value by 1.
#    (ii)  - If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 along with increasing the cnt2 value by 1.
#    (iii) - If the current element and el1 are the same increase the cnt1 by 1.
#    (iv)  - If the current element and el2 are the same increase the cnt2 by 1.
#    (v)   - Other than all the above cases: decrease cnt1 and cnt2 by 1.
# 3) The integers present in el1 & el2 should be the result we are expecting. So, using another loop, we will manually check their counts if they are greater than the floor(N/3).


# Intuition: If the array contains the majority of elements, their occurrence must be greater than the floor(N/3). Now, we can say that the count of minority elements and majority elements is equal up to a certain point in the array. So when we traverse through the array we try to keep track of the counts of elements and the elements themselves for which we are tracking the counts.
# After traversing the whole array, we will check the elements stored in the variables. Then we need to check if the stored elements are the majority elements or not by manually checking their counts.

# Time Complexity: O(N) + O(N), where N = size of the given array.
# Reason: The first O(N) is to calculate the counts and find the expected majority elements. The second one is to check if the calculated elements are the majority ones or not.

# Space Complexity: O(1) as we are only using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.

'''
Question: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

Leetcode Link -> https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

'''

def twoSum(numbers, target):
    """
    Find two numbers in a sorted array that add up to a specific target.

    Since the array is sorted, we can use the two-pointer technique:
    - Start with one pointer at the beginning (left) and one at the end (right)
    - If the sum is less than target, move left pointer right to increase sum
    - If the sum is greater than target, move right pointer left to decrease sum
    - If the sum equals target, we found our solution

    Time Complexity: O(n) - each element is visited at most once
    Space Complexity: O(1) - only using two pointers

    Args:
        numbers: List[int] - sorted array of integers (1-indexed in problem description)
        target: int - target sum to find

    Returns:
        List[int] - 1-indexed positions of the two numbers that add up to target
    """

    # Initialize two pointers: left at start, right at end
    left = 0
    right = len(numbers) - 1

    # Continue until pointers meet or cross
    while left < right:
        # Calculate current sum
        current_sum = numbers[left] + numbers[right]

        # DRY RUN TRACE FOR numbers = [2,7,11,15], target = 9:
        # Iteration 1: left=0 (value=2), right=3 (value=15), sum=17
        #   Since 17 > 9, decrement right -> right=2
        # Iteration 2: left=0 (value=2), right=2 (value=11), sum=13
        #   Since 13 > 9, decrement right -> right=1
        # Iteration 3: left=0 (value=2), right=1 (value=7), sum=9
        #   Since 9 == 9, return [left+1, right+1] = [1, 2]

        # DRY RUN TRACE FOR numbers = [2,3,4], target = 6:
        # Iteration 1: left=0 (value=2), right=2 (value=4), sum=6
        #   Since 6 == 6, return [left+1, right+1] = [1, 3]

        # DRY RUN TRACE FOR numbers = [-1,0], target = -1:
        # Iteration 1: left=0 (value=-1), right=1 (value=0), sum=-1
        #   Since -1 == -1, return [left+1, right+1] = [1, 2]

        if current_sum == target:
            # Found the solution! Return 1-indexed positions
            # Adding 1 to convert from 0-indexed to 1-indexed as required
            return [left + 1, right + 1]
        elif current_sum < target:
            # Sum is too small, need to increase it
            # Move left pointer to the right to get a larger number
            left += 1
        else:
            # Sum is too large, need to decrease it
            # Move right pointer to the left to get a smaller number
            right -= 1

    # According to problem constraints, there is always exactly one solution
    # So we should never reach this point, but returning empty list as fallback
    return []

# Alternative implementation with detailed comments for educational purposes
def twoSum_detailed(numbers, target):
    """
    Detailed version with extensive comments explaining each step.
    This version includes more verbose explanations for learning purposes.
    """

    # POINTER INITIALIZATION
    # We start with two pointers:
    # - left pointer at the beginning of the array (index 0)
    # - right pointer at the end of the array (index len(numbers)-1)
    # This takes advantage of the sorted property of the array
    left = 0
    right = len(numbers) - 1

    # MAIN LOOP
    # Continue looping while left pointer is less than right pointer
    # This ensures we don't use the same element twice (left != right)
    # and we haven't exhausted all possible pairs
    while left < right:
        # Calculate the sum of elements at left and right pointers
        current_sum = numbers[left] + numbers[right]

        # DEBUG TRACE INFORMATION (for understanding)
        # Uncomment the following line to see the step-by-step execution:
        # print(f"Left: {left} ({numbers[left]}), Right: {right} ({numbers[right]}), Sum: {current_sum}")

        # CASE 1: Found the target sum
        if current_sum == target:
            # Since the problem requires 1-indexed positions,
            # we add 1 to convert from 0-indexed array positions
            return [left + 1, right + 1]

        # CASE 2: Current sum is less than target
        # We need a larger sum to reach the target
        # Since the array is sorted in non-decreasing order,
        # moving the left pointer to the right will give us a larger or equal number
        elif current_sum < target:
            # Move left pointer rightward to increase the sum
            left += 1

        # CASE 3: Current sum is greater than target
        # We need a smaller sum to reach the target
        # Since the array is sorted, moving the right pointer leftward
        # will give us a smaller or equal number
        else:
            # Move right pointer leftward to decrease the sum
            right -= 1

    # The problem guarantees exactly one solution exists,
    # so this line should theoretically never be reached
    # However, including it for completeness and to satisfy syntax requirements
    return []

# EDGE CASE ANALYSIS:
# 1. Minimum array size (2 elements):
#    - Works correctly as left=0, right=1, only one iteration possible
#
# 2. Negative numbers:
#    - Works correctly because we're comparing sums, not assuming positive values
#    - Example: [-3, -2, 0, 1, 3], target = -1 -> should find [-3, 2]
#      Actually: -3 + 2 = -1, indices [1, 5] in 1-indexed
#
# 3. Duplicate values:
#    - Works correctly as we move pointers based on sum comparison
#    - Example: [1, 2, 2, 3, 4], target = 4 -> should find [1, 3] (1+3=4)
#      or [2, 2] (2+2=4) depending on which pair we encounter first
#    - Actually finds [2, 3] (2+2=4) since left=1, right=2 gives sum=4
#
# 4. Target at extremes:
#    - Minimum target: works with negative numbers as shown above
#    - Maximum target: works with large positive numbers
#    - Example: [1000, 1000], target = 2000 -> returns [1, 2]
#
# 5. Large array (up to 3*10^4 elements):
#    - Time complexity O(n) handles this efficiently
#    - Space complexity O(1) meets constant space requirement
#
# WHY TWO-POINTER TECHNIQUE IS OPTIMAL:
# - Brute force would be O(n^2) checking all pairs
# - Hash map approach would be O(n) time but O(n) space
# - Two-pointer gives O(n) time and O(1) space - optimal for sorted arrays
# - Takes advantage of the sorted property to eliminate unnecessary checks
# - Each element is examined at most once, making it linear time

# TEST THE FUNCTION WITH EXAMPLES FROM THE PROBLEM STATEMENT
if __name__ == "__main__":
    # Example 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(numbers1, target1)
    print(f"Example 1: numbers = {numbers1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [1, 2]")
    print(f"Correct: {result1 == [1, 2]}\n")

    # Example 2
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = twoSum(numbers2, target2)
    print(f"Example 2: numbers = {numbers2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 3]")
    print(f"Correct: {result2 == [1, 3]}\n")

    # Example 3
    numbers3 = [-1, 0]
    target3 = -1
    result3 = twoSum(numbers3, target3)
    print(f"Example 3: numbers = {numbers3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: [1, 2]")
    print(f"Correct: {result3 == [1, 2]}\n")

    # Additional test cases
    # Test with duplicates
    numbers4 = [1, 2, 2, 3, 4]
    target4 = 4
    result4 = twoSum(numbers4, target4)
    print(f"Additional Test 1: numbers = {numbers4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"One valid solution: [2, 3] (values 2+2=4)\n")

    # Test with larger numbers
    numbers5 = [1000, 1000]
    target5 = 2000
    result5 = twoSum(numbers5, target5)
    print(f"Additional Test 2: numbers = {numbers5}, target = {target5}")
    print(f"Output: {result5}")
    print(f"Expected: [1, 2]")
    print(f"Correct: {result5 == [1, 2]}")
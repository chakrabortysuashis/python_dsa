"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length


LeetCode link: https://leetcode.com/problems/max-consecutive-ones-iii/
"""

"""
APPROACH
Problem in simple words
-----------------------
We have a binary array `nums` and we can flip at most `k` zeros to ones.
Find the maximum length of a contiguous block that can become all 1s.

Brute-force (for understanding)
-------------------------------
Try every subarray and count how many zeros are inside it.
If zeros <= k, update answer.
- Time: O(n^2) subarrays (or O(n^3) if counting zeros naively each time)
- Space: O(1)
Too slow for n up to 10^5.

Why sliding window works
------------------------
A window [left..right] is valid when zeros_count <= k.
So:
1) Move `right` to expand window.
2) Track zeros_count.
3) If invalid, move `left` to shrink window.
4) Keep max window length seen.

Visual pointer notation
-----------------------
index: 0 1 2 3 4 5 6 ...
nums : 1 1 1 0 0 0 1 ...
       L           R
Window is nums[L..R]

Approach 1 (full shrink with while)
-----------------------------------
When zeros_count > k, we keep shrinking in a `while` loop until
window becomes valid again in the same iteration.

Approach 2 (single shrink per iteration)
----------------------------------------
When zeros_count > k, shrink only once (`if`), then move right ahead.
Window may stay invalid briefly, but becomes valid in subsequent steps.
Still O(n), still correct.

=====================================================
DRY RUN 1 (Approach 1): nums=[1,1,1,0,0,0,1,1,1,1,0], k=2
=====================================================
We'll show key steps (L=left, R=right, Z=zeros_count).

Start: L=0, R=0, Z=0, max_len=0

R=0 -> nums[R]=1, Z=0 (valid)
window [0..0], len=1, max_len=1

R=1 -> nums[R]=1, Z=0 (valid)
window [0..1], len=2, max_len=2

R=2 -> nums[R]=1, Z=0 (valid)
window [0..2], len=3, max_len=3

R=3 -> nums[R]=0, Z=1 (valid)
window [0..3], len=4, max_len=4

R=4 -> nums[R]=0, Z=2 (valid)
window [0..4], len=5, max_len=5

R=5 -> nums[R]=0, Z=3 (invalid, Z>k)
Now shrink with while:
- L=0 (nums[L]=1) -> L=1, Z=3
- L=1 (nums[L]=1) -> L=2, Z=3
- L=2 (nums[L]=1) -> L=3, Z=3
- L=3 (nums[L]=0) -> L=4, Z=2 (valid)
window [4..5], len=2, max_len still 5

Continue expanding...
R=6,7,8,9 gives valid windows and max grows to 6.
At R=10 (0), shrink again to remain valid.
Final answer: 6

=====================================================
DRY RUN 2 (Approach 2): nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3
=====================================================
Here we use single-step shrink (`if`), not full `while` shrink.

Start: L=0, R=0, Z=0, max_len=0

R=0 -> 0 => Z=1 (valid), len=1, max_len=1
R=1 -> 0 => Z=2 (valid), len=2, max_len=2
R=2 -> 1 => Z=2 (valid), len=3, max_len=3
R=3 -> 1 => Z=2 (valid), len=4, max_len=4
R=4 -> 0 => Z=3 (valid), len=5, max_len=5
R=5 -> 0 => Z=4 (invalid)
    single shrink: nums[L]=0 so Z=3, L=1
    (no max update this step)
R=6 -> 1 => Z=3 (valid), len=6, max_len=6
R=7 -> 1 => Z=3 (valid), len=7, max_len=7
R=8 -> 1 => Z=3 (valid), len=8, max_len=8
R=9 -> 0 => Z=4 (invalid)
    single shrink: nums[L]=0 so Z=3, L=2
R=10 -> 1 => Z=3 (valid), len=9, max_len=9
R=11 -> 1 => Z=3 (valid), len=10, max_len=10

Later steps never exceed max_len=10.
Final answer: 10
"""


class Solution(object):
    # Approach 1: full-shrink sliding window (classic and easiest to reason about)
    def longestOnes_Approach1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Pointer view:
        index: 0 1 2 3 4 ...
        nums : 1 1 0 1 0 ...
               L       R
        Keep window [L..R] valid with zeros_count <= k.
        """
        left = right = max_len = zeros_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros_count += 1

            # If invalid, keep shrinking until valid again.
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            # Window is valid here.
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

    # Approach 2: single-shrink variant (still O(n), slightly different flow)
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Difference from Approach 1:
        - Approach 1: uses `while zeros_count > k` to fully fix window immediately.
        - Approach 2: uses only one shrink step (`if`) per iteration.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = right = max_len = zeros_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros_count += 1

            if zeros_count > k:
                # Shrink by exactly one step
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            else:
                # Update max only when window is currently valid
                max_len = max(max_len, right - left + 1)

            right += 1

        return max_len


# Final complexity summary for both:
# Time: O(n)
# Space: O(1)



        

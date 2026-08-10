"""
1423. Maximum Points You Can Obtain from Cards
Solved
Medium
Topics
premium lock icon
Companies
Hint
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
 
link -https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

Approach & Working Explanation:
1. **Initial Window (Take all $k$ cards from the left)**:
   - Calculate the sum of the first $k$ elements (`left_sum`).
   - Set `max_sum` to `left_sum`.
   - Initialize `left = k - 1` and `right = len(cardPoints) - 1`.

2. **Sliding / Swapping elements from Left to Right**:
   - Iteratively remove one card from the left side of our window (`left_sum -= cardPoints[left]`, `left -= 1`) and add one card from the extreme right of the array (`right_sum += cardPoints[right]`, `right -= 1`).
   - Track `cur_sum = left_sum + right_sum` at each step and update `max_sum = max(max_sum, cur_sum)`.
   - Continue this process until all elements from the left window have been removed (`left < 0`).

3. **Dry Run Example (`cardPoints = [1,2,3,4,5,6,1], k = 3`)**:
   - Initial `left_sum` of first 3 elements `[1, 2, 3]` = `6`. `max_sum = 6`.
   - Iteration 1: Remove `3` from left, add `1` from right $\rightarrow$ `left_sum = 3`, `right_sum = 1`, `cur_sum = 4`, `max_sum = 6`.
   - Iteration 2: Remove `2` from left, add `6` from right $\rightarrow$ `left_sum = 1`, `right_sum = 7`, `cur_sum = 8`, `max_sum = 8`.
   - Iteration 3: Remove `1` from left, add `5` from right $\rightarrow$ `left_sum = 0`, `right_sum = 12`, `cur_sum = 12`, `max_sum = 12`.
   - Final Result: `12`.
"""

def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left=k-1
        right=len(cardPoints)-1
        cur_sum=left_sum=right_sum=max_sum=0
        # leftsum = sum of the first of first k elements  
        for i in range(0,k):
            left_sum+=cardPoints[i]
        # this left sum vbecomes the max sum
        max_sum=left_sum
        # now keep on removing 1 elements from left pointer in left sum and at the same time add one element from right pointer into right sum.
        # keep continuing this until we remove all the left pointer elements ie left sum is 0 anbd only eight elements aree present.
        while (left>=0):
            left_sum=left_sum-cardPoints[left]
            left-=1
                
            right_sum+=cardPoints[right]
            right-=1

            cur_sum=left_sum+right_sum
            max_sum=max(max_sum,cur_sum)
        return max_sum

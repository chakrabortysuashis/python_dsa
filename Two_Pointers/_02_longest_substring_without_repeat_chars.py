
"""
Problem: Longest Substring Without Repeating Characters
Technique: Sliding Window with Hash Map

Overview:
The sliding window approach maintains a window [left, right] that contains only unique characters.
We expand the window by moving `right` to the right one character at a time.
If we encounter a character that is already present in our current window (tracked via a hash map
storing the most recent index of each character), we must shrink the window from the left.
Crucially, when a duplicate character is found at index `right` whose previous occurrence was at
`last_seen_index`, we can instantly jump `left` to `max(left, last_seen_index + 1)`.
This avoids redundant steps and ensures the left pointer never moves backwards.
"""

"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
 
link-https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Array/Hash map to store the last seen index of each character (-1 initially)
        hash_map = [-1] * 256
        left = right = max_len = 0
        
        while right < len(s):
            # Check if the element is a duplicate and the duplicate lies within the current substring window
            if hash_map[ord(s[right])] != -1 and hash_map[ord(s[right])] >= left:
                # The duplicate lies within the substring; advance left past the previous occurrence
                left = hash_map[ord(s[right])] + 1
                
            max_len = max(max_len, right - left + 1)
            
            # Regardless of whether the char was seen before, store/update the latest position of char
            hash_map[ord(s[right])] = right
            right += 1
            
        return max_len

# ==========================================
# DRY RUN TRACE WITH EXAMPLE: "abcabcbb"
# ==========================================
# Initial State: s = "abcabcbb", left = 0, right = 0, max_len = 0
# - right=0 ('a'): not in map. max_len = max(0, 0-0+1) = 1. map['a'] = 0. right=1
# - right=1 ('b'): not in map. max_len = max(1, 1-0+1) = 2. map['b'] = 1. right=2
# - right=2 ('c'): not in map. max_len = max(2, 2-0+1) = 3. map['c'] = 2. right=3
# - right=3 ('a'): seen at 0 >= left(0). left = 0+1 = 1. max_len = max(3, 3-1+1) = 3. map['a'] = 3. right=4
# - right=4 ('b'): seen at 1 >= left(1). left = 1+1 = 2. max_len = max(3, 4-2+1) = 3. map['b'] = 4. right=5
# - right=5 ('c'): seen at 2 >= left(2). left = 2+1 = 3. max_len = max(3, 5-3+1) = 3. map['c'] = 5. right=6
# - right=6 ('b'): seen at 4 < left(3)? No, 4 >= 3. left = 4+1 = 5. max_len = max(3, 6-5+1) = 3. map['b'] = 6. right=7
# - right=7 ('b'): seen at 6 >= left(5). left = 6+1 = 7. max_len = max(3, 7-7+1) = 3. map['b'] = 7. right=8
# Final Result: 3

# ==========================================
# COMPLEXITY ANALYSIS
# ==========================================
# Time Complexity: O(N) where N is the length of string s. The right pointer traverses once.
# Space Complexity: O(min(N, Σ)) where Σ = 256 (ASCII character space size).


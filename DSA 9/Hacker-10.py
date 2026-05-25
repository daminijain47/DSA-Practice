# Palindrome Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        rev = 0
        save = x

        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10

        return rev == save
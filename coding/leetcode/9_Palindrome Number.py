"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        inputNum = x
        newNum = 0
        while x>0:
            newNum = newNum * 10 + x%10
            x = x//10
        return newNum == inputNum

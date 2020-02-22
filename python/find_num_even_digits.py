#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution(object):
    def findNumbers(self, nums):
        even = 0
        for i, num in enumerate(nums):
            if len(str(nums[i]))%2 == 0:
                even += 1
            else:
                even += 0
        return even
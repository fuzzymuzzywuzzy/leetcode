#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution(object):
    def balancedStringSplit(self, s):
        s_list = [char for char in s]
        R_count, L_count, balanced = 0, 0, 0

        for i, n in enumerate(s_list):
            if s_list[i] == 'R':
                R_count += 1
            else:
                L_count += 1

            if L_count == R_count:
                balanced += 1
                R_count, L_count = 0, 0

        return balanced
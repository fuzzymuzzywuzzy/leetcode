#https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, J, S):
        J_list = [jewel for jewel in J]
        S_list = [stone for stone in S]
        JewelsInStones = [stone for stone in S_list if stone in J_list]
        return len(JewelsInStones)
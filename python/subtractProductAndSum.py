#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution(object):
    def subtractProductAndSum(self, n):

        n_digits = [int(d) for d in str(n)]
        n_product = 1
        n_sum = 0

        for n in n_digits:
            n_product = n_product*n

        for n in n_digits:
            n_sum = n_sum+n

        return n_product-n_sum
# Question number -- 2778
# Title -- Sum-of-Squares-of-Special-Elements
# To return the sum of squares of all special elements in the array where special numbers mean it divides the length of the array leaving remainder 0.

# Approach -- 1
# Thought of first iterating through the array and then storing them in a list and then squaring them and finally summing them up.
# Not an optimal approach since we are traversing the array twice.

# Approach -- 2
# Directly iterating through the array and checking if the element divides the length of the array.If it does then we square it and add it to the sum variable

# Code 


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total_sum = 0
        length = len(nums)

        for i in range(length):
            if length % (i+1) == 0:
                total_sum += nums[i] * nums[i]
                # or use 
                # total_sum += nums[i] ** 2

        return total_sum

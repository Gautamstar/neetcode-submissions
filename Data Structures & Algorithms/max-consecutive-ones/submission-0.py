class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_con = 0
        for i in nums:
            if i == 1:
                counter += 1
                if max_con < counter:
                    max_con = counter
            else:
                counter = 0
        return max_con
                
        
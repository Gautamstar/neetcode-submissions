class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for index, number in enumerate(nums):
            if number in seen:
                return True
            else:
                seen[number] = index
        return False

        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Empty dict {key: value as num:num_count}
        # as I iterate through the nums, 
        # check if num_count > 1, return true else false

        num_count = {}

        for num in nums:
            if num in num_count:
                return True 
            else:
                num_count[num] = 1
        return False 

            

        
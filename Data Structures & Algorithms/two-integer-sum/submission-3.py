class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input = array
        # output = indices of two nums that adds to the target 

        # I need to remember diff of target - num
        # I need keep track of current num and it's index and also look for diff as I loop
        # I can use hashmap key:value as num:index of its num

        num_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_index: 
                return [num_index[diff], i]
            else:
                num_index[num] = i




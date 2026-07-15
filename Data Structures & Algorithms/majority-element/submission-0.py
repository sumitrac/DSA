class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #  max_element = len(nums) / 2 -- this always exist so no need to write it

        #  I need to keep count of each element and the num itself
        #  compare when count is greater, than return the num of greater count

        num_count = {} # 5:4, 1:3

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        for k, v in num_count.items():
            if v > len(nums) / 2:
                return k 
        
            


        
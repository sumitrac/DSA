class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # now need to return top k keys
        return sorted(num_count, key=lambda num:num_count[num])[-k:]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num_count = {}
        # for num in nums:
        #     if num in num_count:
        #         num_count[num] += 1
        #     else:
        #         num_count[num] = 1

        # # now need to return top k keys
        # return sorted(num_count, key=lambda num:num_count[num])[-k:]

        # Time: NLogN with sort 
        # Space: LogN with hashmap

        # with hashmpa and bucket sort
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # creates a empty [] for the lend of bucket 
        bucket = [[] for _ in range(len(nums)+1)]

        # assign values in bucket
        for num in num_count:
            bucket[num_count[num]].append(num)
        
        # return top k 
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result














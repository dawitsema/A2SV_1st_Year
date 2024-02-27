class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dictionary = defaultdict(int)
        count = 0
        checker = set(nums)

        pt = 0
        for i in range(len(nums)):
            dictionary[nums[i]] += 1
            while len(dictionary) == len(checker):
                count += len(nums) - i
                if dictionary[nums[pt]] > 1:
                    dictionary[nums[pt]] -= 1
                else:
                    del dictionary[nums[pt]]
                pt += 1
        
        return count

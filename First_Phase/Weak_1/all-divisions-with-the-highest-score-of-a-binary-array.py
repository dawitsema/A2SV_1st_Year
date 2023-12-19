from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize variables to keep track of counts and scores
        count_0_left = 0
        count_1_right = nums.count(1)
        max_score = 0
        max_indices = []

        # Iterate through indices and calculate scores
        for i in range(n + 1):
            if i > 0:
                count_0_left += (nums[i - 1] == 0)
                count_1_right -= (nums[i - 1] == 1)

            current_score = count_0_left + count_1_right

            # Update maximum score and indices
            if current_score > max_score:
                max_score = current_score
                max_indices = [i]
            elif current_score == max_score:
                max_indices.append(i)

        return max_indices

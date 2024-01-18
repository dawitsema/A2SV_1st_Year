from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        left, max_length = 0, 0
        max_repeat_count = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            max_repeat_count = max(max_repeat_count, char_count[s[right]])

            while (right - left + 1) - max_repeat_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

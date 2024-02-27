class Solution:
    def bestClosingTime(self, customers: str) -> int:
        nums1 = [1 if customer == "Y" else 0 for customer in customers]
        nums2 = [0 if n else 1 for n in nums1]

        suffix = [0] * (len(nums1) + 1)
        for i in range(len(nums1) - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums1[i]

        prefix = [0]
        for i in range(len(nums2)):
            prefix.append(prefix[-1] + nums2[i])

        ans = -1
        minn = float("inf")
        for i in range(len(prefix)):
            if prefix[i] + suffix[i] < minn:
                ans = i
                minn = prefix[i] + suffix[i]

        return ans

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        if len(nums1) < len(nums2):
            dic2 = Counter(nums2)
            for i in range(len(nums1)):
                if nums1[i] in dic2:
                    ans.append(nums1[i])
                    if dic2[nums1[i]] > 1:
                        dic2[nums1[i]] -= 1
                    else:
                        del dic2[nums1[i]]
        else:
            dic1 = Counter(nums1)
            for i in range(len(nums2)):
                if nums2[i] in dic1:
                    ans.append(nums2[i])
                    if dic1[nums2[i]] > 1:
                        dic1[nums2[i]] -= 1
                    else:
                        del dic1[nums2[i]]

        return ans

                    

        
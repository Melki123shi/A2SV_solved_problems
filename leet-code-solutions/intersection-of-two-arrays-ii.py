class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        result = []
        for num in n1:
            if num in n2:
                result.extend([num for _ in range(min(n1[num], n2[num]))])
        return result

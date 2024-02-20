class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monotonic_stack = []
        hashs = {}

        for num in nums2[::-1]:
            while monotonic_stack and monotonic_stack[-1] <= num:
                monotonic_stack.pop()

            if not monotonic_stack:
                hashs[num] = -1
            else:
                hashs[num] = monotonic_stack[-1]

            monotonic_stack.append(num)

        for i in range(len(nums1)):
            nums1[i] = hashs[nums1[i]]

        return nums1
        


            




           


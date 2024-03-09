class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        left_max = 0
        right_max = 0

        while left <= right:
            if right_max < left_max:
                value = right_max - height[right]
                if value > 0:
                    result += value
                right_max = max(right_max, height[right])
                right -= 1

            else:
                value = left_max - height[left]
                if value > 0:
                    result += value
                left_max = max(left_max, height[left])
                left += 1

        return result
            
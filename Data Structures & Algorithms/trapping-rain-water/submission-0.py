class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left, right = 0, n - 1
        leftSide,rightSide = height[left], height[right]
        total = 0

        while left < right:
            if leftSide < rightSide:
                left += 1
                leftSide = max(leftSide, height[left])
                total += leftSide - height[left]
            else:
                right -= 1
                rightSide = max(rightSide, height[right])
                total += rightSide - height[right]
        return total
        
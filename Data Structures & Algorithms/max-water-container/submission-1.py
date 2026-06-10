class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxAmount = 0
        left = 0
        right = n - 1
        while left <= right:
            leftSide, rightSide = heights[left], heights[right]
            currArea = computeArea(left, right, heights)
            maxAmount = max(maxAmount, currArea)
            if leftSide > rightSide:
                right -= 1
            else:
                left += 1

        return maxAmount

def computeArea(i,j, arr):
    return (j - i) * min(arr[i], arr[j])
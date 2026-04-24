class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = computeVolume(heights, left, right)

        while left <= right:
            print(left, right)
            left_side = heights[left]
            right_side = heights[right]
            if left_side < right_side:
                left +=1
            else:
                right -=1
            area = max(area, computeVolume(heights, left, right))

        return area



def computeVolume(heights, i, j):
    width = j - i 
    height = min(heights[i], heights[j])
    return width * height
        
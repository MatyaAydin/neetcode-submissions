class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        n1 = len(nums1)
        if n1 % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2])  / 2
class Solution:
	def findMin(self, nums):
		# 1, 2, 3, 4, 5, 6
		# 6, 1, 2, 3, 4, 5
		# 5, 6, 1, 2, 3, 4
		# (low, mid) in left, (high) in right: n[low] < n[mid], n[high] < n[low]
		# (low) in left, (mid, high) in right n[mid] < n[high], n[high] < n[low]
		# move low and high to encapsulate the cutoff index

		n = len(nums)
		low = 0
		high = n - 1
		while low < high:
			mid = (low + high) // 2
			if nums[mid] < nums[high]:
				high = mid
			else:
				low = mid + 1
		return nums[low]
				
			

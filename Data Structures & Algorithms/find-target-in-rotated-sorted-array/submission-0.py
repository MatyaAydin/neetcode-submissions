class Solution:
	def search(self, nums, target):
		# 1, 2, 3, 4, 5, 6
		# 6, 1, 2, 3, 4, 5
		# 5, 6, 1, 2, 3, 4
		# 4, 5, 6, 1, 2, 3
		# low > mid > high: (mid high) in right subarray
		#
		# low < mid, high < low, high < mid: (low, mid) in left subarray
		#  target > high: target in left subarray
		
		n = len(nums)
		low = 0
		high = n - 1
		while low <= high:
			mid = (high + low) // 2
			if nums[mid] == target:
				return mid
			if nums[low] <= nums[mid]: # left is sorted
				if nums[low] <= target < nums[mid]: # in left:
					high = mid - 1
				else: # in right
					low = mid + 1
					
			else: # right is sorted:
				if nums[mid] < target <= nums[high]: # in right
					low = mid + 1
				else:
					high = mid - 1
		return - 1
			

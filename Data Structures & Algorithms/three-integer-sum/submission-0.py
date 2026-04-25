
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            # Optimization: If the smallest number is > 0, no triplet can sum to 0
            if nums[i] > 0:
                break
                
            # Error Fix: Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum == 0:
                    # Error Fix: Store values, not indices
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Error Fix: Skip duplicate values for 'left' and 'right'
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return triplets
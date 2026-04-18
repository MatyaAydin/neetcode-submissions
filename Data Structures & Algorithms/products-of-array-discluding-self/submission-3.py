class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 zero: 0 everywhere, full prod at 0 index
        more than one zero: 0 everywhere
        """

        full_prod = 1
        has_zero = 0
        for n in nums:
            if n != 0:
                full_prod *= n
            else:
                has_zero += 1

        if has_zero == 1:
            return [0 if n != 0 else full_prod for n in nums]
        elif has_zero > 1:
            return [0] * len(nums)
        else:
            return [full_prod // n for n in nums]
        
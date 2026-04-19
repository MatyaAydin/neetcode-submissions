class Solution:
    def isHappy(self, n: int) -> bool:

        seen_numbers = set()
        curr = n
        while curr not in seen_numbers:
            if curr == 1:
                return True
            seen_numbers.add(curr)
            curr = get_squared_sum(curr)

        return False



def get_squared_sum(n):

    sum_ = 0
    curr = n
    while curr:
        digit = curr % 10
        curr //= 10
        sum_ += digit**2


    return sum_
        
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addNext = False
        index = len(digits) - 1
        digits[index] += 1
        if digits[index] == 10:
            addNext = True
            while index >= 1 and  addNext:
                digits[index] = 0
                digits[index - 1] += 1
                if digits[index - 1] != 10:
                    addNext = False
                index -=1
            if addNext:
                digits[0] = 0
                digits = [1] + digits
                
        return digits


            
        
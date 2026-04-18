class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:


        wallet = {
            5: 0,
            10: 0,
        }

        for dollar in bills:

            if dollar == 5:
                wallet[5] +=1

            elif dollar == 10:
                if wallet[5] == 0:
                    return False
                else:
                    wallet[5] -=1
                    wallet[10] +=1

            else:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -=1
                    wallet[5] -=1

                elif wallet[5] >= 3:
                    wallet[5] -=3
                else:
                    return False

                # must give 15 back: can do 3*5 or 10+5. first try with 10 becuase 5 must also be used for 10


        return True
        
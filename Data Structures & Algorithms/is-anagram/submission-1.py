class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        occ_s = return_occ(s)
        occ_t = return_occ(t)


        return occ_s == occ_t

    
def return_occ(s):
    occ = {}
    for char_ in s:
        if char_ not in occ:
            occ[char_] = 0
        occ[char_] +=1
    return occ
        
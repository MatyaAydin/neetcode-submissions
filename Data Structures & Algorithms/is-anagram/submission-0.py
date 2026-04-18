class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        occ_s = return_occ(s)
        occ_t = return_occ(t)


        for char_ in occ_s.keys():
            if char_ not in occ_t:
                return False
            if occ_t[char_] != occ_s[char_]:
                return False

        for char_ in occ_t.keys():
            if char_ not in occ_s:
                return False
            if occ_t[char_] != occ_s[char_]:
                return False
        return True

    
def return_occ(s):
    occ = {}
    for char_ in s:
        if char_ not in occ:
            occ[char_] = 0
        occ[char_] +=1
    return occ
        
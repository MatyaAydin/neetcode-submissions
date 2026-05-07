class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occ = {}
        n = len(s)
        begin = 0
        end = 0
        longest = 0
        while end < n:
            occ[s[end]] = occ.get(s[end], 0) + 1
            mostCommon = max(occ, key=occ.get)
            different = (end - begin + 1 - occ[mostCommon])
            while begin <= end and  different > k:
                # print(s[begin:end+1])
                occ[s[begin]] -= 1
                begin +=1
                mostCommon = max(occ, key=occ.get)
                different = (end - begin + 1 - occ[mostCommon])
            longest = max(longest, end - begin + 1)

            
            end +=1
        return longest


        
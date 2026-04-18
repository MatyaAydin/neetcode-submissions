class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        occ = {}
        for n in nums:
            if n not in occ:
                occ[n] =0
            occ[n] +=1

        unique_vals = occ.keys()
        return sorted(unique_vals, key = lambda v: -occ[v])[:k]
        
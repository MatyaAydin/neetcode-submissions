class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        anagram_to_idx = {}
        current_idx = 0
        for word in strs:
            hash_ = get_hash(word)
            if hash_ not in anagram_to_idx:
                anagram_to_idx[hash_] = current_idx
                groups.append([word])
                current_idx +=1
            else:
                groups[anagram_to_idx[hash_]].append(word)
        return groups




def get_hash(s):
    arr = [0] * 26
    for c in s:
        arr[ord(c) - ord('a')] += 1
    return tuple(arr)
        
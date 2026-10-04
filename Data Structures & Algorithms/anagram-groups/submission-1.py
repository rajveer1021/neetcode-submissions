class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for s in strs:
            char_set = [0]*26
            for char in s:
                char_set[ord('a')- ord(char)] += 1
            key = tuple(char_set)
            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(s)
        return (list(hashmap.values()))

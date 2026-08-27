class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for word in strs:
            anagram_word = ''.join(sorted(word))
            anagramMap[anagram_word].append(word)
        return list(anagramMap.values())
        
        
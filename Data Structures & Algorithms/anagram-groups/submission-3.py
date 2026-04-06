class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping_dict = defaultdict(list)
        for word in strs:
            letter_list = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                letter_list[index] += 1
            letter_tuple = tuple(letter_list)
            mapping_dict[letter_tuple].append(word)
        return list(mapping_dict.values())
            

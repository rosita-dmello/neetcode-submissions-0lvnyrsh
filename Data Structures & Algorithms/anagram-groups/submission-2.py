class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping_dict = {}
        for word in strs:
            letter_list = [0] * 26
            for letter in word:
                # hashmap of the word 
                index = ord(letter) - ord('a')
                letter_list[index] += 1
            letter_tuple = tuple(letter_list)
            mapping_dict[letter_tuple] = mapping_dict.get(letter_tuple,[]) + [word]

        return list(mapping_dict.values())
            

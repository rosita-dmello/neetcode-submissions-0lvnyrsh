class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}
        ga = []
        for i in range(len(strs)):
            pa = []
            pa.append(strs[i])
            if visited.get(i, 0) == 1:
                continue
            visited[i] = 1
            for j in range(i+1, len(strs)):
                if (sorted(strs[i]) == sorted(strs[j])):
                    pa.append(strs[j])
                    visited[j] = 1
            ga.append(pa)
        return ga
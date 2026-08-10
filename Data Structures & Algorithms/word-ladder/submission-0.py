class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        ptrn_map = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                ptrn_map[pattern].append(word)
        q = collections.deque()
        q.append(beginWord)
        res = 1
        visited = set([beginWord])

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    neighbours = ptrn_map[pattern]
                    for n in neighbours:
                        if n in visited:
                            continue
                        visited.add(n)
                        q.append(n)
            res += 1
        return 0

                
                            
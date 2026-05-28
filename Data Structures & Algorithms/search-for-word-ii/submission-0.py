class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (r >= rows or c >= cols or r<0 or c<0 or board[r][c] not in node.children or (r,c) in visited):
                return
            visited.add((r,c))
            char = board[r][c]
            node = node.children[char]
            word += char
            if node.end:
                res.add(word)
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)

        
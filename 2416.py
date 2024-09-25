class TrieNode:
    def __init__(self):
        self.children = dict()
        self.n = 0
    
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
            curr.n += 1
    
    def traverse(self, word):
        output = 0

        curr = self
        for c in word:
            curr = curr.children[c]
            output += curr.n

        return output

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for word in words:
            root.insert(word) 
        
        answer = []
        for word in words:
            answer.append(root.traverse(word))
        
        return answer
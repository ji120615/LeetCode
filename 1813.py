class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1

        i = 0
        while i < l1 and s1[i] == s2[i]:
            i += 1
        
        return s1[i : l1] == s2[l2 - (l1 - i) : l2]
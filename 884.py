class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = Counter(map(str, (s1 + ' ' + s2).split()))

        return set(e for e in s3 if s3[e] == 1)
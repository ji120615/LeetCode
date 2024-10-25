class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        answer = [folder[0]]
        for e in folder[1:]:
            if e.startswith(answer[-1] + '/'):
                continue
            else:
                answer.append(e)
        
        return answer
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = len(skill) // 2

        total = sum(skill)
        if total % l != 0:
            return -1
        target = total // l

        skill.sort()
        product = 0
        for i in range(l):
            if skill[i] + skill[-(i + 1)] != target:
                return -1
            
            product += skill[i] * skill[-(i + 1)]
        
        return product
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill)-1
        checker = skill[left] + skill[right]
        chem_sum = 0
        while left < len(skill)//2:
            if checker == skill[left] + skill[right]:
                chem_sum += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1

        return chem_sum
        
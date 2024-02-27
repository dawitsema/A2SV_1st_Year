class Solution:
    def maxScore(self, s: str) -> int:
        s_list = [int(x) for x in s]

        zero_count = [0]
        for i in range(len(s_list)):
            if s_list[i] == 0:
                zero_count.append(zero_count[-1] + 1)
            else:
                zero_count.append(zero_count[-1])

        one_count = [0] * (len(s_list) + 1)
        for i in range(len(s_list) - 1, -1, -1):
            one_count[i] = one_count[i + 1] + s_list[i]

        maxx = 0
        for i in range(1, len(one_count) - 1):
            maxx = max(maxx, one_count[i] + zero_count[i])

        return maxx

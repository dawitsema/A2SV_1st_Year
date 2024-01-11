class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count1 = max1 = flip1 = 0
        pt1 = 0

        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                flip1 += 1

            while flip1 > k:
                if answerKey[pt1] == "T":
                    flip1 -= 1
                count1 -= 1
                pt1 += 1
            count1 += 1
            max1 = max(count1, max1)


        count2 = max2 = flip2 = 0
        pt2 = 0

        for i in range(len(answerKey)):
            if answerKey[i] == "F":
                flip2 += 1

            while flip2 > k:
                if answerKey[pt2] == "F":
                    flip2 -= 1
                count2 -= 1
                pt2 += 1
            count2 += 1
            max2 = max(count2, max2)
            
        return max(max1, max2)
        
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num = sorted(str(num))
            zero_count = num.count('0')
            zero_no = zero_count
            
            while zero_count > 0:
                num.remove('0')
                zero_count -= 1

            zeros = [0]*zero_no
            zeros.insert(0, num[0])
            zeros.extend(num[1:])
            nm = 0
            for i in zeros:
                nm *= 10
                nm += int(i)

            return nm
        elif num < 0:
            num = sorted(str(num), reverse = True)
            zero_count = num.count('0')
            zero_no = zero_count
            num.remove('-')
            
            while zero_count > 0:
                num.remove('0')
                zero_count -= 1

            zeros = [0]*zero_no
            num.extend(zeros)
            nm = 0
            for i in num:
                nm *= 10
                nm += int(i)

            return nm * -1
        else:
            return num


        
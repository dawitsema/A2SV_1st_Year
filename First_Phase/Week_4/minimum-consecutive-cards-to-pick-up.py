class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minn = len(cards)
        left = 0
        check = set()
        count = 0
        
        flag = False
        for i in range(len(cards)):
            count += 1
            if cards[i] not in check:
                check.add(cards[i])

            else:
                flag = True
                while cards[i] != cards[left]:
                    count -= 1
                    check.remove(cards[left])
                    left += 1
                minn = min(count, minn)
                left += 1
                count -= 1
            
            
        return minn if flag is True else -1



        
class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        time = self.dictionary[key]

        left, right = 0, len(time) - 1
        ans = ""
        while left <= right:
            midd = (left + right) // 2

            if time[midd][0] <= timestamp:
                ans = time[midd][1]
                left = midd + 1
            else:
                right = midd - 1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

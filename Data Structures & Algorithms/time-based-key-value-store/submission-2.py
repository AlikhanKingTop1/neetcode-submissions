class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        need = float("inf")
        l = 0
        r = len(self.store[key]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.store[key][mid][0] <= timestamp:
                need = mid
                l = mid+1
            else:
                r = mid -1
        if need == float("inf"):
            return ""
        else:
            return str(self.store[key][need][1])


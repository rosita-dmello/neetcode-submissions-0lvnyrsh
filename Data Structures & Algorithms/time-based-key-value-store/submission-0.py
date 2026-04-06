class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store[key] 
        l = 0
        r = len(vals) - 1
        res = ""
        while l <= r:
            mid = l + ((r-l)//2)
            mid_ts = vals[mid][0]
            if mid_ts == timestamp:
                return vals[mid][1]
            elif mid_ts > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = vals[mid][1]
        return res
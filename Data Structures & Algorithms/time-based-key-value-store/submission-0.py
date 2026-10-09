class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[timestamp], [value]]
        else:
            self.store[key][0].append(timestamp)
            self.store[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        ts = self.store[key][0]
        vals = self.store[key][1]

        l = 0
        r = len(ts)

        while l < r:
            m = l + (r - l) // 2
            if ts[m] > timestamp:
                r = m
            else:
                l = m + 1
        
        return vals[r-1] if r > 0 else ""

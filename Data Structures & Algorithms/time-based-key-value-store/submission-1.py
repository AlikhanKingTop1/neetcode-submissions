class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(lambda: defaultdict(list))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key][timestamp] = value
    def get(self, key: str, timestamp: int) -> str:
        if timestamp not in self.hashmap[key]:
            need = 0
            for i in self.hashmap[key]:
                if i <= timestamp:
                    need = i
            if need == 0:
                return ""
            else:
                return str(self.hashmap[key][need])

        return str(self.hashmap[key][timestamp])

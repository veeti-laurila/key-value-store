import threading
import uuid

# https://algodaily.com/lessons/designing-a-simple-key-value-store-af5f4c6a
class keyValueStore:
    uuidValue = uuid.uuid4()
    def __init__(self):
        self.store = {}
    # https://www.youtube.com/watch?v=fu2cD_6E8Hw
    def set(self, key: str, value: str, uuid) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, str(uuid)])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        left, right = 0, len(values) -1
        while left <= right:
            middle = left+right // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle +1
            else:
                right = middle-1


        return result



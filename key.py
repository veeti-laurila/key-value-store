import threading
import uuid

# https://algodaily.com/lessons/designing-a-simple-key-value-store-af5f4c6a
class keyValueStore:
    uuidValue = uuid.uuid4()
    def __init__(self):
        self.store = {}
        self.lock = threading.Lock()
    # https://www.youtube.com/watch?v=fu2cD_6E8Hw
    def set(self, key: str, value: str) -> str:
        time_uuid = str(uuid.uuid4())
        with self.lock:
            if key not in self.store:
                self.store[key] = []
            # https://www.uuidgenerator.net/dev-corner/python
            self.store[key].append([value, time_uuid])
        return time_uuid

    def get(self, key: str, time_uuid) -> str:
        result = ""
        values = self.store.get(key, [])
        left, right = 0, len(values) -1
        while left <= right:
            middle = left+right // 2
            if values[middle][1] <= time_uuid:
                result = values[middle][0]
                left = middle +1
            else:
                right = middle-1


        return result



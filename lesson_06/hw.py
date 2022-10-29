import time


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.order = 0
        self.t = time.time()


class LRUCache:

    def __init__(self, limit=42):
        self.items = []
        self.count = 0
        self.limit = limit

    def get(self, key):
        for item in self.items:
            if item.key == key:
                item.order += 1
                item.t = time.time()
                time.sleep(0.0001)
                return item.value
        return None

    def get_min_value_idx(self, field, idx_array):
        min_value = float("inf")
        idx = 0

        for temp_idx in idx_array:
            item = self.items[temp_idx]

            if field == "order":
                temp_value = item.order
            else:
                temp_value = item.t

            if temp_value < min_value:
                min_value = temp_value
                idx = temp_idx

        return idx

    def get_idx_list(self, min_value):
        idx_array = []
        for idx, item in enumerate(self.items):
            if item.order == min_value:
                idx_array.append(idx)
        return idx_array

    def set(self, key, value):
        item = Item(key, value)

        if self.count == self.limit:

            # get idx of item with minimal order
            min_value_idx = self.get_min_value_idx(field="order", idx_array=range(len(self.items)))

            # minimal order value
            min_value_order = self.items[min_value_idx].order

            # get the indexes of items with order == minimal_order_value
            idx_array = self.get_idx_list(min_value_order)

            # remove from elements with minimal order the item which has minimal time attribute
            remove_idx = self.get_min_value_idx(field="time", idx_array=idx_array)

            # add new element
            self.items[remove_idx] = item

        else:
            self.items.append(item)
            self.count += 1

    def info(self):
        for item in self.items:
            print(item.key, item.order, item.t)


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"

    cache.set("k3", "val3")

    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"
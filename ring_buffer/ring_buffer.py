class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []    # list for items
        self.index = 0

    def append(self, item):
        # add item to storage when there is capacity
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        # otherwise overwrite oldest
        else:
            self.storage[self.index] = item
            self.index += 1
            # ring around the storage
            if self.index == self.capacity:
                self.index = 0

    def get(self):
        # get items in storage
        return [item for item in self.storage if item]
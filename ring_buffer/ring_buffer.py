class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []    # List for items
        self.index = 0

    def append(self, item):
        # go to the end of the list
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        # add the item to the list
        else:
            self.storage[self.index] = item
            self.index += 1

            # when capacity is reached overwrite the oldest
            if self.index == self.capacity:
                self.index = 0

    def get(self):
        # get items in stoarge
        return [item for item in self.storage if item]
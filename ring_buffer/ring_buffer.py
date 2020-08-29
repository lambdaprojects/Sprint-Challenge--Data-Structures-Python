from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity

        # Current will be the item that has to be replaced in the ring buffer
        self.current = None
        self.storage = DoublyLinkedList()
        pass

    def append(self, item):
        pass

    def get(self):
        pass

print("------RING BUFFER-------")
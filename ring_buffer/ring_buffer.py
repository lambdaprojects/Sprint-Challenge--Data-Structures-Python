from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity

        # Current will be the item that has to be replaced in the ring buffer
        self.current = None
        self.storage = DoublyLinkedList()
        pass
    

    def append(self, item):
        #Check if the length is less than the capacity. If so it does not need any replacement.
        # It just needs to be added to the double linked list
        # Also if the length is the same as capacity then the first item pushed in will be the
        # one to be replaced.
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            if (self.storage.length == self.capacity):
                self.current = self.storage.head
        else:
            if (self.current is self.storage.head):
                print("------CURRENT IS HEAD ----------")
                self.storage.head.value = item
                self.current = self.storage.head.next
            elif (self.current is self.storage.tail):
                print("------CURRENT IS TAIL ----------")
                self.storage.tail.value = item
                self.current = self.storage.head
            else:
                i = 1
                current_node = self.storage.head
                # We will be traversing the DLL and replace the value
                # To do this we will need to create a new DLL and keep adding the values 
                # from old list and change the value which equals current
                print("------CREATING NEW DLL TO REPLACE----------")
                print("------CURRENT ITEM TO REPLACE IS ----", self.current.value)
                new_dll = DoublyLinkedList()
                is_value_updated = False
                while (i<self.storage.length+1):
                    if (self.current.value is current_node.value and not is_value_updated):
                        current_node.value = item
                        if (current_node.next is None):
                            self.current = self.storage.head
                        else:
                            self.current = current_node.next
                        is_value_updated = True
                    new_dll.add_to_tail(current_node.value)
                    i += 1
                    current_node = current_node.next
                self.storage = new_dll

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        i = 1
        current_node = self.storage.head
        while (i < self.storage.length + 1):
            if (current_node.value is not None):
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next
            i += 1

        return list_buffer_contents

ring_buffer = RingBuffer(5)
ring_buffer.append('a')
ring_buffer.append('b')
ring_buffer.append('c')
ring_buffer.append('d')
print(ring_buffer.storage.length)
print(ring_buffer.get())
ring_buffer.append('e')
print(ring_buffer.storage.length)
print(ring_buffer.get())
ring_buffer.append('f')
print(ring_buffer.storage.length)
print(ring_buffer.get())
ring_buffer.append('g')
print('------ADDING H AND I-----')
ring_buffer.append('h')
ring_buffer.append('i')
print(ring_buffer.storage.length)
print(ring_buffer.get()) #['f', 'g', 'h', 'i', 'e']

ring_buffer.append('j')
print(ring_buffer.storage.length)
print(ring_buffer.get()) 
ring_buffer.append('k')
print(ring_buffer.get()) #['k', 'g', 'h', 'i', 'j']
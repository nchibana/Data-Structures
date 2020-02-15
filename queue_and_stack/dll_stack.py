import sys
sys.path.append('C:/Users/nchib/DS5/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.len() > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

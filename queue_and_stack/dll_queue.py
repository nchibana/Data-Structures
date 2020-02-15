import sys
sys.path.append('C:/Users/nchib/DS5/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.len() > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

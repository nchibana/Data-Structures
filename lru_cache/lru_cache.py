from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList
from collections import OrderedDict

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.no_nodes = 0
        self.dll = DoublyLinkedList()
        self.storage = OrderedDict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage:
            return None
        else:
            node = self.storage[key]
            value = node.value
            self.dll.delete(node)
            node = ListNode(key, value)
            self.storage[key] = node
            self.dll.add_to_head(key, value)
            return node.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key not in self.storage:
            node = ListNode(key, value)
            self.storage[key] = node
            if self.no_nodes < self.limit:
                self.dll.add_to_head(key, value)
                self.no_nodes += 1
            else:
                curr_tail = self.dll.remove_from_tail()
                self.storage.pop(curr_tail.key)
                self.dll.add_to_head(key, value)
        else:
            node = self.storage[key]
            self.dll.delete(node)
            node = ListNode(key,value)
            self.storage[key] = node
            self.dll.add_to_head(key, value)

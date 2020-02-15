"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, key, value):
        current_next = self.next
        self.next = ListNode(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, key, value):
        if self.length > 0:
            #create new node and insert before head
            self.head.insert_before(key, value)
            #update self.head
            self.head = self.head.prev
            self.length += 1
        elif self.length == 0:
            self.head = ListNode(key, value)
            self.tail = self.head
            self.length += 1
        

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length > 0:
            ret_val = self.tail.value
            new_tail = self.tail.prev
            self.delete(self.tail)
            self.tail = new_tail
            return ret_val


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length == 0:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node.prev is None:
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
        node.delete()
        self.length -= 1

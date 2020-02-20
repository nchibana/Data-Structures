import sys
sys.path.append('C:/Users/nchib/DS5/Data-Structures/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return
        
        #BST was empty
        elif self.value is None:
            self.value = BinarySearchTree(value)
        
        #insert into right search tree
        elif value >= self.value:
            #TBC
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        #insert into left subtree
        else:
            #TBC
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        elif self.value is None:
            return False

        else: 
            if target >= self.value:
                self.right.contains(target)
            else:
                self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left is None:
            return self.value.cb
        elif self.right is None:
            return self.value.cb
        else:
            self.right.for_each()
            self.left.for_each()
        
        #1. Base case:
        #left is None or Right is None

        #2. Recursive case:
        # Go Left and Right

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

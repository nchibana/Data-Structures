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

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # cur = self

        # while cur.right is not None:
        #     cur = cur.right

        # return cur.value
        
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #call function on current node
        cb(self.value)

        #recursive case
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        #base case
        # else both are none, stop recursion
        
    # def iter_for_each(self, cb):
    #     if self is None:
            #print msg, BST is empty
            # return

        #root node
        # cb(self.value)
        #add left child to stack if exists
        #add right child to stack if exists

        #all other nodes
        # while len(stack) > 0: # still nodes left
            # pop top of stack
            # cb (top of stack)
            #go left .. if left child, push onto stack
            #go right .. if right child, push onto stack
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left root right

        # base case
        # we're at the bottom of the tree
        # node is none or has no children
        if node is None:
            return

        # recursive case
        # go left as far as possible
        self.in_order_print(node.left)
        print(node.value)
        # go right as far as possible
        self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.size != 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.size != 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

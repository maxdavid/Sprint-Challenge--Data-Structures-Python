class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        parent = self
        node = BinarySearchTree(value)
        while True:
            if value < parent.value:
                if parent.left:
                    parent = parent.left  # traverse down left
                else:
                    parent.left = node
                    break
            else:
                if parent.right:
                    parent = parent.right  # traverse down right
                else:
                    parent.right = node
                    break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while node.value != target:
            if target < node.value and node.left:
                node = node.left
            elif target >= node.value and node.right:
                node = node.right
            else:
                break
        return node.value == target

    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        while node.right:
            node = node.right
        return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        node = self
        cb(node.value)
        if node.left:
            node.left.for_each(cb)
        if node.right:
            node.right.for_each(cb)
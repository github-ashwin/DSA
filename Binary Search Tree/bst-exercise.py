"""
1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
"""

class BST:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def search(self,val):
        
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def inorder_traversal(self): # Left, Root, Right
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def preorder_traversal(self): # Left, Root, Right
        elements = [self.data]

        # elements.append(self.data)

        if self.left:
            elements += self.left.inorder_traversal()

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def postorder_traversal(self): # Left, Root, Right
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        if self.right:
            elements += self.right.inorder_traversal()
        
        elements.append(self.data)

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
        
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
        
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum +right_sum

def build_tree(elements):
    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.inorder_traversal())
    print("Pre order traversal:", numbers_tree.preorder_traversal())
    print("Post order traversal:", numbers_tree.postorder_traversal())
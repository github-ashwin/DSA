class BST:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            # add to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            # add to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def inorder_traversal(self): # Left, Root, Right
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                False

def build_tree(elements):

    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,19,34]
    tree = build_tree(numbers)
    print(tree.inorder_traversal())
    print(tree.search(2))
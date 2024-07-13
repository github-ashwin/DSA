class Tree:

    def __init__(self,data):
        self.data = data
        self.children = [] # Every child of a tree is an instance of Tree
        self.parent = None

    def add_child(self,child):
        child.parent = self # Assigning to the instance
        self.children.append(child) # Adding to the list

    def get_level(self): # Get the level of nodes using parent
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3 # Getting spaces
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children: # If there is child, it moves further
            for child in self.children:
                child.print_tree() # Recursion

def product_tree():

    root = Tree("Electronics")

    laptop = Tree("Laptop")
    laptop.add_child(Tree("Macbook"))
    laptop.add_child(Tree("Windows"))
    laptop.add_child(Tree("Linux"))

    mobile = Tree("Mobile")
    mobile.add_child(Tree("iOS"))
    mobile.add_child(Tree("Android"))

    console = Tree("Console")
    console.add_child(Tree("Play Station"))
    console.add_child(Tree("Xbox"))
    console.add_child(Tree("Nintendo"))

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(console)

    return root

if __name__ == '__main__':
    root = product_tree()
    root.print_tree()
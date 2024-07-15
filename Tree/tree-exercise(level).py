class Tree:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self,level):

        if self.get_level() > level:
            return
        
        spaces = ' ' * self.get_level() * 3 
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.children: 
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = Tree("Global")

    india = Tree("India")

    gujarat = Tree("Gujarat")
    gujarat.add_child(Tree("Ahmedabad"))
    gujarat.add_child(Tree("Baroda"))

    karnataka = Tree("Karnataka")
    karnataka.add_child(Tree("Bangluru"))
    karnataka.add_child(Tree("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = Tree("USA")

    nj = Tree("New Jersey")
    nj.add_child(Tree("Princeton"))
    nj.add_child(Tree("Trenton"))

    california = Tree("California")
    california.add_child(Tree("San Francisco"))
    california.add_child(Tree("Mountain View"))
    california.add_child(Tree("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(3)
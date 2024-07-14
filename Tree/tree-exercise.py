class Tree:

    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self,condition):

        if condition == 'name':
            value = self.name
        elif condition == 'designation':
            value = self.designation
        elif condition == 'both':
            value = self.name + ' ' + self.designation
        else:
            value = self.name + ' ' + self.designation


        spaces = ' ' * self.get_level() * 3 
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + value)
        if self.children: 
            for child in self.children:
                child.print_tree(condition) 

def build_management_tree():
        # CTO Hierarchy
        infra_head = Tree("Vishwa","Infrastructure Head")
        infra_head.add_child(Tree("Dhaval","Cloud Manager"))
        infra_head.add_child(Tree("Abhijit", "App Manager"))

        cto = Tree("Chinmay", "CTO")
        cto.add_child(infra_head)
        cto.add_child(Tree("Aamir", "Application Head"))

        # HR hierarchy
        hr_head = Tree("Gels","HR Head")

        hr_head.add_child(Tree("Peter","Recruitment Manager"))
        hr_head.add_child(Tree("Waqas", "Policy Manager"))

        ceo = Tree("Nilupul", "CEO")
        ceo.add_child(cto)
        ceo.add_child(hr_head)

        return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    print('\n')
    root_node.print_tree("designation")
    print('\n')
    root_node.print_tree("both")
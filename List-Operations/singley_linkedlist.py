class Node:
    def __init__(self, data):
        """Initialize the node with data and next as None."""
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize the LinkedList with head pointing to None."""
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Point new node's next to current head
        self.head = new_node  # Update head to new node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        last = self.head  # Start from the head node
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node  # Point the last node's next to the new node

    def insert_after_node(self, prev_node, data):
        """Insert a new node after the given prev_node."""
        if not prev_node:  # If the given node is None, cannot insert
            print("The given previous node is not in the LinkedList.")
            return
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = prev_node.next  # Point new node's next to prev_node's next
        prev_node.next = new_node  # Point prev_node's next to the new node

    def delete_node_by_value(self, key):
        """Delete the first node with the given value."""
        current = self.head  # Start from the head node
        previous = None  # Initialize previous node as None

        if not current:  # If the list is empty, nothing to delete
            return

        if current.data == key:  # If the head node holds the key
            self.head = current.next  # Update head to the next node
            current = None  # Delete the current node
            return

        while current and current.data != key:  # Traverse the list
            previous = current
            current = current.next

        if not current:  # If the key was not found in the list
            return

        previous.next = current.next  # Unlink the node from the list
        current = None  # Delete the current node

    def delete_node_by_position(self, position):
        """Delete the node at the given position."""
        if not self.head:  # If the list is empty, nothing to delete
            return

        temp = self.head  # Start from the head node

        if position == 0:  # If the head node needs to be deleted
            self.head = temp.next  # Update head to the next node
            temp = None  # Delete the head node
            return

        for i in range(position - 1):  # Traverse to the node before the position
            temp = temp.next
            if not temp:
                return

        if not temp.next:  # If the position is out of bounds
            return

        next = temp.next.next  # Point to the node after the one to be deleted
        temp.next = None  # Unlink the node to be deleted
        temp.next = next  # Link to the next node

    def traverse(self):
        """Traverse and print the list."""
        temp = self.head  # Start from the head node
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def search(self, key):
        """Search for a node with the given key."""
        current = self.head  # Start from the head node
        while current:
            if current.data == key:  # If the node's data matches the key
                return True
            current = current.next
        return False

# Example usage:
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_beginning(2)
ll.insert_at_end(3)
ll.insert_after_node(ll.head, 4)  # Inserts 4 after the first node (which is 2)
ll.traverse()  # Output: 2 -> 4 -> 1 -> 3 -> None
print(ll.search(3))  # Output: True
ll.delete_node_by_value(1)
ll.traverse()  # Output: 2 -> 4 -> 3 -> None
ll.delete_node_by_position(1)
ll.traverse()  # Output: 2 -> 3 -> None

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:  # Handles empty list case
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:  # Handles empty list case
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, given_node_data, data):
        current = self.head
        while current:
            if current.data == given_node_data:
                new_node = Node(data, current.next, current)
                current.next = new_node
                if new_node.next:  # Update prev of the next node if it exists
                    new_node.next.prev = new_node
                else:  # If inserted at the end, update tail
                    self.tail = new_node
                return  # Important: Exit after insertion
            current = current.next
        # If given_node_data is not found, you might want to raise an exception or print a message.
        print(f"Node with data {given_node_data} not found.")


    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete_first(self):
        if self.head is None:
            return  # Nothing to delete
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        if self.tail is None:
            return  # Nothing to delete
        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_item(self, item):
        current = self.head
        while current:
            if current.data == item:
                if current == self.head:
                    self.delete_first()
                elif current == self.tail:
                    self.delete_last()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # Important: Exit after deletion
            current = current.next
        print(f"Item {item} not found in the list.")

    def is_empty(self):
        return self.head is None

    def print_DLL(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result



DLL1 = DLL()
DLL1.insert_at_start(10)
DLL1.insert_at_start(20)
DLL1.insert_at_start(30)
DLL1.insert_at_start(40)
DLL1.insert_at_start(50)
DLL1.insert_at_start(60)
DLL1.insert_at_start(70)
DLL1.insert_at_start(80)
DLL1.insert_at_start(90)
DLL1.insert_at_start(100)
DLL1.insert_at_last(110)
DLL1.insert_after(50, 55)
DLL1.delete_item(80) 
result = DLL1.print_DLL()
print(result)
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_start(self, item):
        new_node = Node(item)
        new_node.next = self.head  # Correct insertion logic
        self.head = new_node

    def insert_at_last(self, item):
        new_node = Node(item)
        if self.head is None:  # Handle empty list case
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def search(self, item):
        current = self.head  # Start from the head
        while current:
            if current.data == item:
                return current  # Return the node if found
            current = current.next
        return None  # Return None if not found

    def insert_after(self, new_item, prev_item):
        new_node = Node(new_item)
        current = self.head
        while current:
            if current.data == prev_item:
                new_node.next = current.next
                current.next = new_node
                return  # Exit after insertion
            current = current.next
        print(f"Node with data {prev_item} not found.")  # Indicate if prev_item not found

    def delete_first(self):
        if self.head is None:  # Handle empty list
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None or self.head.next is None:  # Handle empty or single-node list
            self.head = None
            return

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_item(self, item):
        if self.head is None:
            return  # Nothing to delete

        if self.head.data == item:  # Delete from the beginning
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == item:
                current.next = current.next.next
                return  # Exit after deletion
            current = current.next
        print(f"Item {item} not found in the list.")  # Indicate if item not found


    def printLL(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


SLL1 = SLL()
SLL1.insert_at_start(10)
SLL1.insert_at_start(5)
SLL1.insert_at_last(100)
SLL1.insert_after(20, 10)
SLL1.delete_item(10)  # Now works correctly
SLL1.delete_last() # Now works correctly
SLL1.delete_first() # Now works correctly

result = SLL1.printLL()
print(result)
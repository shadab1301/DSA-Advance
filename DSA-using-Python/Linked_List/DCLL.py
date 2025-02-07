# Doubly circular linked list
class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
class CDLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def is_empty(self):
        return self.head==None
    def search(self,data):
        if not self.is_empty():
            if self.head != self.tail:
                # Linked list has more than one item
                if self.tail.data==data:
                    return self.tail
                curr_node=self.head
                while curr_node != self.tail:
                    if curr_node.data==data:
                        return curr_node
                    curr_node=curr_node.next
            else:
                # Linkedlist has only one node
                if self.head.data==data:
                    return self.head
            return None
    def insert_at_start(self,data):
        if self.is_empty():
            new_node=Node(None,data,None)
            new_node.next=new_node
            new_node.prev=new_node
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(self.head.prev,data,self.head)
            self.tail.next=new_node
            self.head.prev=new_node
            self.head=new_node
    def insert_at_last(self,data):
        if self.is_empty():
            new_node=Node(None,data,None)
            new_node.next=new_node
            new_node.prev=new_node
            self.head=new_node
            self.tail=new_node
        else:
              new_node=Node(self.tail,data,self.head)
              self.tail.next=new_node
              self.head.prev=new_node
              self.tail=new_node
    def insert_after(self,temp_node,data):
        if temp_node is not None:
            if temp_node==self.tail:
                # if temp_node is tail
                self.insert_at_last(data)
            else:
                new_node=Node(temp_node,data,temp_node.next)
                curr_node=self.head
                while curr_node != self.tail:
                    if curr_node==temp_node:
                        temp_node.next.prev=new_node
                        temp_node.next=new_node
                        break
                    curr_node=curr_node.next
    def delete_first(self):
        if not self.is_empty():
            if self.head != self.tail:
                # Linked list has more than one node
                self.tail.next=self.head.next
                self.head.next.prev=self.tail
                self.head=self.head.next
            else:
                # Linked list has only one node
                self.head=None
                self.tail=None
    def delete_last(self):
        if not self.is_empty():
            if self.head != self.tail:
                # Linked list has more than one node
                self.tail.prev.next=self.head
                self.head.prev=self.tail.prev
                self.tail=self.tail.prev
            else:
                # Linked list has only one node
                self.head=None
                self.tail=None
    def delete_item(self,item):
        if not self.is_empty():
            if self.head==self.tail:
                # Linkedlist has only one node
                if self.head.data==item:
                    self.head=None
                    self.tail=None
                    return
            else:
                # Linkedlist has more than one Node
                curr_node=self.head.next
                while curr_node != self.head:
                    if curr_node.data==item:
                        curr_node.prev.next=curr_node.next
                        curr_node.next.prev=curr_node.prev
                        curr_node.next=None
                        curr_node.prev=None
                        break
                    curr_node=curr_node.next
                # Now checking for last node => tail
                if curr_node.data==item:
                    self.delete_last()
    def print_all(self):
        result=[]
        if not self.is_empty():
            curr_node=self.head
            while curr_node != self.tail:
                result.append(curr_node.data)
                curr_node=curr_node.next
            result.append(curr_node.data)
        return result

cdll1=CDLL()
cdll1.insert_at_start(10)
cdll1.insert_at_start(20)
cdll1.insert_at_last(30)
cdll1.insert_at_last(40)
cdll1.insert_after(cdll1.search(10),50)
cdll1.insert_after(cdll1.search(20),100)
cdll1.insert_after(cdll1.search(40),200)
# 20 10 50 30 40

result=cdll1.print_all()
print(result)

    
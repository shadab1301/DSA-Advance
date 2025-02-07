# Singly circular linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class CSLL:
    def __init__(self):
        self.tail=None
    def is_empty(self):
        return self.tail==None
    def insert_at_start(self,data):
        new_node=Node(data)
        if self.tail is not None:
            new_node.next=self.tail.next
            self.tail.next=new_node
        else:
            self.tail=new_node
            new_node.next=new_node
    def insert_at_last(self,data):
         new_node=Node(data)
         if self.tail is not None:
            new_node.next=self.tail.next
            self.tail.next=new_node
            self.tail=new_node
         else:
              self.tail=new_node
              new_node.next=new_node
    def search(self,data):
        if self.is_empty():
            return None
        else:
            curr_node=self.tail.next
            while curr_node != self.tail:
                if curr_node.data==data:
                    return curr_node
                curr_node=curr_node.next
            if curr_node.data==data:
                return curr_node
            return None
    def insert_after(self,ref_node,data):
        if ref_node is not self.is_empty():   
            new_node=Node(data,ref_node.next)
            ref_node.next=new_node
            if ref_node==self.tail:
                self.tail=new_node
        else:
            raise IndentationError("ref_node should not be 'None'")
    def print_all(self):
        result=[]
        if not self.is_empty():
            curr_node=self.tail.next
            while curr_node != self.tail:
                result.append(curr_node.data)
                curr_node=curr_node.next
            
            result.append(curr_node.data)
        return result
    def delete_first(self):
        if not self.is_empty():
            if self.tail==self.tail.next:
                self.tail=None
            else:
                self.tail.next=self.tail.next.next
    def delete_last(self):
         if not self.is_empty():
             if self.tail==self.tail.next:
                 self.tail=None
             else:
                 second_last_node=self.tail.next
                 while second_last_node.next != self.tail:
                     second_last_node=second_last_node.next
                 second_last_node.next=self.tail.next
                 self.tail=second_last_node
    def delete_item(self,item):
        if not self.is_empty():
            if self.tail==self.tail.next:
                # Linked list has only one node
                if self.tail.data==item:
                    self.tail=None
            else:
                # Linked list has multiple Node
                if self.tail.next.data==item:
                    # delete 1st node
                    self.delete_first()
                elif self.tail.data==item:
                    # delete last node
                    self.delete_last()
                else:
                    prev_node=self.tail.next
                    while prev_node != self.tail:
                        if prev_node.data==item:
                            prev_node.next=prev_node.next.next
                            prev_node.next.next=None
                            break
                        prev_node=prev_node.next
    
    
    
cll=CSLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
cll.insert_after(cll.search(20),100)
cll.insert_after(cll.search(40),200)
# 20 10 50 30 40

result=cll.print_all()
print(result)
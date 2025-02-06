class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def is_empty(self):
        if self.head==None and self.tail==None:
            return True
        else:
            return False
    def insert_at_start(self,data):
        new_node=Node(None,data,self.head)
        if self.head != None:
            self.head.prev=new_node
        else:
            self.tail=new_node
        self.head=new_node
    def insert_at_last(self,data):
        new_node=Node(self.tail,data,None)
        if self.tail is not None:
            self.tail.next=new_node
        self.tail=new_node

    def insert_after(self,tempNode,data):
           if tempNode is not None:
                new_node=Node(tempNode,data,tempNode.next)
                if tempNode.next is not None:
                    tempNode.next.prev=new_node
                    tempNode.next=new_node
                else:
                     tempNode.next=new_node
    def search(self,given_data):
        if given_data is not None:
            curr=self.head
            while curr is not None:
                if curr.data==given_data:
                    return curr
                curr=curr.next
            return None

    def delete_first(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head.next.prev=None
            self.head=self.head.next
    def delete_last(self):
        if self.head is not None:
            if self.tail.prev is not None:
                self.tail.prev.next=None
            self.tail.prev=None
        
    def delete_item(self,data):
        if data is not None:
            if self.head is not None:
                if self.head.next is not None:
                    # LL has more than one node
                    curr_node=self.head
                    while curr_node is not None:
                        if curr_node.data==data:
                            if curr_node.data == self.tail.data:
                                print(f"{data} I am from tail")
                                curr_node.prev.next=None
                                self.tail=curr_node.prev
                            elif curr_node.data==self.head.data:
                                print(f"{data} I am from head")
                                curr_node.next.prev=None
                                self.head=curr_node.next
                                curr_node.next=None
                            else:    
                                print(f"{data} I am in between head and tail")
                                curr_node.next.prev=curr_node.prev
                                curr_node.prev.next=curr_node.next
                                curr_node.next=None
                                curr_node.prev=None
                        curr_node=curr_node.next
                else:
                    # LL has more exaclt one node
                    if self.head.data==data:
                        self.head=None
                        self.tail=None

            else:
                # Mean LL is already empty
                pass


    def print_DLL(self):
        result=[]
        curr_node=self.head
        while curr_node is not None:
            result.append(curr_node.data)
            curr_node=curr_node.next
        return result



DLL1=DLL()

DLL1.insert_at_start(10)
# print(DLL1.is_empty())
DLL1.insert_at_start(20)
DLL1.insert_at_start(30)
DLL1.insert_at_start(40)
DLL1.insert_at_start(50)
DLL1.insert_at_start(60)
DLL1.insert_at_last(70)
DLL1.insert_after(DLL1.search(30),990)
DLL1.delete_first()
DLL1.delete_last()
result=DLL1.delete_item(40)
result=DLL1.delete_item(990)
result=DLL1.delete_item(50)
# result=DLL1.delete_item(10)   some error occured
result=DLL1.print_DLL()

print(result)


# delete_first,delete_last,delete_item
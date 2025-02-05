class Node{
    constructor(item=null,next=null){
        this.item=item
        this.next=next
    }
}
class SLL {
    constructor(head){
    }
}

// Add item in start
SLL.prototype.add_In_start=function(data){
    // Create Node
   let new_node=Node(data)
    // case 1: Linkedlist is empty
    if(!this.head){
        this.head=node
    }else{
        new_node.next=this.head
        this.head=new_node
    }
}

// Add item at Last
SLL.prototype.insert_at_last=function(data){
    let new_node=Node(data)
    if(!this.head){
        this.head=new_node
        return
    }
    let currNode= this.head
    while(currNode.next){
        currNode=currNode.next
    }
    currNode.next=new_node
}

// Add item at given node
SLL.prototype.insert_at_given_node=function(data,given_node){
    let new_node=Node(data,given_node.next)
    given_node.next=new_node
}

// Delete first Node
SLL.prototype.deleteFirstNode=function(){
    if(!this.head){
        console.log("Linked list is Empty")
        return
    }
    this.head=this.head.next
}

// Delete last Node
SLL.prototype.deleteLast_Node=function(){
    if(!this.head){
        console.log("Linked list is empty")
        return
    }
    if(!this.head.next){
        this.head=null
    }
    let secondLastNode=this.head
    while(secondLastNode.next.next){
        secondLastNode=secondLastNode.next
    }
    secondLastNode.next=null
}

// delete by key
SLL.prototype.deleteByKey=function(given_node){
    let currNode=this.head
    while(currNode.next.next){
        if(currNode.next.item == given_node.item){
            currNode.next=secondLastNode.next.next
        }
        currNode=currNode.next
    }
    
}

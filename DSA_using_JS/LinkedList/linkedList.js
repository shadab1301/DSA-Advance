class Node{
    constructor(data,next=null){
        this.data=data
        this.next=next
    }
}

class LinkedList{
    constructor(){
        this.head=null
    }  
}

LinkedList.prototype.insertAtBeginning=function(data){
    const newNode= Node(data)
    this.head=newNode
}
LinkedList.prototype.insertAtlast=function(data){
    const newNode= Node(data)
    if(!this.head){
        this.head=newNode
        return
    }
    let tail= this.head
    while(tail.next){
        tail=tail.next
    }
    tail.next=newNode
}

LinkedList.prototype.insertAtGivenNode=function(data,prevNode){
    if(!prevNode){
        console.log("PrevNode Cannot be null")
        return
    }
    const newNode= new Node(data,prevNode.next)
    prevNode.next=newNode

}
LinkedList.prototype.deleteFirstNode=function(){
    if(!this.head) return 
    this.head=this.head.next 
}
LinkedList.prototype.deleteLastNode=function(){
    if(!this.head) return 
    if(!this.head.next){
        this.head=null
        return
    }
    let secondLastNode=this.head
    while(secondLastNode.next.next){ 
        secondLastNode=secondLastNode.next
    }

    secondLastNode.next=null
}

LinkedList.prototype.deleteByKey=function(key){
    if(!this.head) return
    if(this.head.data===key){
        this.head=this.head.next
        return
    }
    let currentNode=this.head
    while(currentNode.next){
        if(currentNode.next.data===key){
            currentNode.next=currentNode.next.next
            return
        }
        currentNode=currentNode.next
    }
}

LinkedList.prototype.isNodeAvailable=function(key){
    if(!this.head) return
    if(this.head.data===key) return true
    let current=this.head
    while(current){
        if(current.data===key){
            return true
        }
        current=current.next
    }
    return false
}

LinkedList.prototype.printList=function(){
    if(!this.head) return
    let result=[]
    let current=this.head
    while(current){
        result.push(current.data)
        current=current.next
    }

    return result.join(" => ")
}

LinkedList.prototype.reverseLinkedList=function(){
    if(!this.head) return
    let currentNode = this.head
    let previousNode =null
    let nextNode = null
    while(currentNode){
        nextNode=currentNode.next
        currentNode.next=previousNode
        previousNode=currentNode
        currentNode=nextNode
    }
    this.head=previousNode
}

 

class Node:
     def __init__(self,data=None,next=None):
           self.data=data
           self.next=next
class LinkedList:
      def __init__(self,head=None):
            self.head=head
      def insert_items(self,data):
          newNode = Node(data)
          if (self.head):
              currentNode = self.head
              while (currentNode.next != None):
                    
                     currentNode=currentNode.next
              currentNode.next=newNode
          else :
               self.head  =newNode  
              
      def pritnItems(self):
           currentNode = self.head
           while(currentNode):
                 print(currentNode.data)   
                 currentNode=currentNode.next
ll = LinkedList()
n = int(input())
for i in range(n):
    a = input()
    ll.insert_items(a)
ll.pritnItems()                              
                        
                        
                        
                            
           
        

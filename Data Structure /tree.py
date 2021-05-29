class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 

def lca(root,n1,n2):
         if(root.data> n1 and root.data > n2):
             lca(root.left,n1,n2)
         elif(root.data<n1 and root.data<n2):
             lca(root.right,n1,n2)
         return root        
                       
          
def inorder(root):
     
       if root is None  :
          return 
       inorder(root.left) 
       print(root.data) 
       inorder(root.right) 

def insert(root,data):
     if(root is None):
        root = Node(data)
     else :
          if(root.data>data):
              if(root.left is None):
                  root.left = Node(data)
              else :
                   insert(root.left,data)
          else :
                if(root.right is None):
                  root.right = Node(data)
                else :
                    insert(root.right,data) 
def swap(root,level,k):
    if(root is None ):
        return 
    if((level+1)%k == 0):
        root.right ,root.left = root.left,root.right
    swap(root.left,level+1,2)
    swap(root.right,level+1,2)        
                                                                      
root = Node(50)                       
insert(root,30)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,60)
insert(root,80)

inorder(root)
#temp = lca(root,49,4100)
#print(temp.data)
#print(t.insert(root= None,56))
swap(root,1,1) 
print("after swapping node ")
inorder(root)     


                    

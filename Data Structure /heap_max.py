# Heap_max is represented by only array ..............  it's posible to represend array and tree(recursion) 


import sys
class  Heap_max:
    def __init__(self,maxsize):
         self.size = 0 
         self.maxsize = maxsize
         self.heap = [0]*(self.maxsize+1)
         self.heap[0] = sys.maxsize
    def swap(self,a,b):
       temp = self.heap[a]
       self.heap[a] = self.heap[b] 
       self.heap[b] = temp
    def parent(self,pos):
       return pos//2
    def insert(self,ele):
        if(self.size >= self.maxsize):
           return 
        self.size += 1
        self.heap[self.size] = ele
        current = self.size
        while(self.heap[current] > self.heap[self.parent(current)]):
             self.swap(current, self.parent(current))
             current = self.parent(current)     
             
    def print(self) :
        for i in range(1,(self.size//2)+1):
           print("parent ----> "+ str(self.heap[i]) +" left subtree----> " + str(self.heap[2*i]) + " right substree--->" + str(self.heap[2*i + 1]))          
h = Heap_max(15)
h.insert(33)
h.insert(55)
h.insert(12)
h.insert(44)
h.insert(22)                     
h.print()         


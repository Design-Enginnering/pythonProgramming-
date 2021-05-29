#!/usr/bin/env python

quicksort(a,first,last):
   i = first
   j = last
   p = first
   if i < j:
     while i < j :
      while a[p] >= i :
         i = i+1
      while a[p] < j ;
         j =j-1
      if i < j :
         temp = a[i]
         a[i] = a[j]  
         a[j] = temp
   temp = a[p]
   a[p] = a[j]
   a[j] = temp
   quick(a,first,j-1)
   quick(a,j+1,last)      
           

List= []
size = input("Enter size of list for quick sort ")
print("Enter elements for quick sort ")
for i in range(size):
    element = input()
    List.append(element)
  
quicksort(List,0,len(List)-1)
print(List)  



































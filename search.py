def linearSearch(l,x):
   for i in range(len(l)):
      if l[i] == x:
         return l[i]
   return -1 

List = [2,3,5,7,9,11,13,17,19]
searchElement = int(input("Enter value for searching in list\n"))
find_element = linearSearch(List,searchElement)
if(find_element == -1): 
    print("Element "+str(searchElement)+" isn't found") 
else :
    print("Element "+str(find_element)+" is found")


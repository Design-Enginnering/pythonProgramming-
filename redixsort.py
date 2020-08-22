def redix_sort(l,maxdigit):
   i ,j = 0,0
   new_list = []
   while len(l) > i :
        length = len(str(l[j]))
        inttostring = str(l[j])
        append_zero = maxdigit-length
        while length != maxdigit :
            inttostring = "0"+inttostring
            length = length +1
        new_list.append(inttostring)   
        print int(new_list[0])
        j = j+1    
        i = i+1    
   print new_list   



List  = [12,8,890,99]
Max = List[0] 
for i in range(1,len(List)):
    if Max < List[i]:
       Max = List[i] 
maxdigit= len(str(Max))

redix_sort(List,maxdigit)       
      

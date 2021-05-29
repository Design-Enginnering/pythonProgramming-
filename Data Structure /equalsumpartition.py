def equalsumpartitionSet(Set,s,n) :
    if s == 0 :
       return True 
    elif s != 0 and n ==0 :
       return False    
    elif Set[n-1] <= s :
         return equalsumpartitionSet(Set,s,n-1) or equalsumpartitionSet(Set,s-Set[n-1],n-1) 
    else : 
         return equalsumpartitionSet(Set,s,n-1)        


def partitionSet(Set,n):
    s = 0  
    for i in range(0,n):
      s = Set[i] + s
    if s % 2 != 0 :
       return False 
    return equalsumpartitionSet(Set,s/2,n)     




Set = [9,1,3,6,5,2]
n = len(Set)
print partitionSet(Set,n)


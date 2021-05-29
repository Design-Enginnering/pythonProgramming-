
def subsetsum(l,n,s):
     if s == 0 :
         return True  
     elif n == 0 and s != 0 : 
        return False 
     elif l[n-1] > s:
        return subsetsum(l,n-1,s)
     else :
        return subsetsum(l,n-1,s) or  subsetsum(l,n-1,s-l[n-1])           
 
l = [4,2,3,9,6,2,1]
n = len(l)
s = 9
print subsetsum(l,n,s)


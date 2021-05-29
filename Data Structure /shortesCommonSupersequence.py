# shorts common supersequestion (scs) string(a) and string(b) common part and remender part add in new variable and print out ----> but both string are order mainten if those string no continues then no problem. but order mainted.
# a = abcde
# b = abcxy
# order maintend if it's not continues then problem.   c = a+b -LCS --> c = abcdexy

def lcs(x,y,n,m):
   if n == 0 or m == 0 :
      return 0
   elif x[n-1] == y[m-1] :
        
        return   lcs(x,y,n-1,m-1)
       
   else : 
        return (lcs(x,y,n-1,m) +  lcs(x,y,n,m-1))        
def superSequention(x,y,n,m) :
    return lcs(x,y,n,m)  
x="krishna"
y="krippna"
print superSequention(x,y,len(x),len(y))    

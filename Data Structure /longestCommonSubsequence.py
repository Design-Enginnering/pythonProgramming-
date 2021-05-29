def Max(a,b) :
     if a>b :
        return a
     else :
        return b     

def sequence(x,y,n,m):
   if n == 0 or m == 0 :
      return 0
   elif x[n-1] == y[m-1] :
        return 1 + sequence(x,y,n-1,m-1)
   else : 
        return Max(sequence(x,y,n,m-1),sequence(x,y,n-1,m))
                




x = "krishna"
y = "vishal"
print sequence(x,y,len(x),len(y))

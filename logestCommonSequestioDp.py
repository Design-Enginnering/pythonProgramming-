def lcsDp(x,y,n,m):
     M = [[ -1 for j in range(m+1)]  for i in range(n+1)]
     for i in range(n+1):
        for j in range(m+1):
            if i ==0 or j == 0 :
                M[i][j] = 0
            elif x[i-1] == y[j-1] :
                  M[i][j] = 1+M[i-1][j-1]
                 
            else :
                 M[i][j] = max(M[i][j-1],M[i-1][j])
                   
   
     lcs = [['']*(m+1)]*(n+1)           
     i ,j = n,m
     while i > 0 and j > 0 : 
         if x[i-1] == y[j-1] :
             lcs[i-1][j-1] = x[i-1]
             i -=1
             j -=1
         elif M[i-1][j] > M[i][j-1] :
                i-=1
         else : 
               j -=1            
     print "LCS of " + x +" and "+ y + " is " + " " + str(lcs)      
     
     
     
     return M[n][m]            
                           
x = "krishna"
y = "vishna"
n = len(x)
m = len(y)

print lcsDp(x,y,n,m)


def subsetSumDp(l,s,n):
    k = [  [ False  for j in range(s+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
           if i == 0  :
              k[i][j]  = False
           elif j == 0:
              k[i][j] = True 
           
           elif l[i-1] <= j :
               k[i][j] = k[i-1][j] or k[i-1][s-l[i-1]]
           else :
               k[i][j] = k[i-1][j]   
                         
    return k[n][s]


l = [3,1,9]
n = len(l)
s = 9 
print subsetSumDp(l,s,n)

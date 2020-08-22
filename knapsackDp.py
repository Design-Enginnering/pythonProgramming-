def Max(a,b):
   if a>b:
     return a 
   else : 
     return b   


def knapsack(wt,value,n,w):
    k = [[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
           if i ==0 or j == 0 :
              k[i][j] = 0 
           elif wt[i -1 ] <= w :
               k[i][j] = Max(value[i-1]+k[i-1][w-wt[i-1]],k[i-1][j])
           elif wt[i-t] > w :
                k[i][j] = k[i-1][j]        
    print n 
    print w  
    return k[n][w]
 



wt = [30,10,9,10]
value = [10,30,2,3]
n = len(wt)
w = 50
print knapsack(wt,value,n,w)



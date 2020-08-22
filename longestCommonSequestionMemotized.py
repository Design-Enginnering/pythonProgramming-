# Longest command sequestion recursion and memorize that means dyanamic program(dp) and recursion both are mix in program . memorize means if recurion one time perform and result same next node then store in array of metrix. it is called memorize programm.this isn't full DP that is only recursion and metrix .full DP programms only include metrix no have recurition call.
def lcsMemorize(x,y,n,m):
    M = [[ -1 for j in range(m+1)]for i in range(n+1)]
    if n == 0 or m == 0 :
       return M[n][m]
    elif x[n-1] == y[m-1] :
         return M[n][m] = (1+ lcsMemorize(x,y,n-1,m-1))    
    else :
         return M[n][m] = max(lcsMemorize(x,y,n,m-1),lcsMomorize(x,y,n-1,m))     




x = "krishna"
y = "prince"
n = len(x)
m = len(y)

print lcsMemorize(x,y,n,m)

def equalsumpartition(Set,s,n):
    k = [[ False for j in range(s+1)] for i in range(n+1)]
    for i in range(n+1) :
       for j in range(s+1) :
          if i == 0 :
             k[i][j] = False 
          elif j == 0 : 
             k[i][j] = True 
          elif Set[i-1] <= s :
              k[i][j] = k[i-1][s-Set[i-1]] or k[i-1][j]
          else : 
              k[i][j] = k[i-1][j]      
    return k[n][s]              


def partition(Set,n) :
    s = 0
    for i in range(n):
       s = Set[i] + s
    if s % 2 != 0 :
        return False 
    return equalsumpartition(Set,s/2,n)     
          




Set = [9,2,3,4,2,8] 
n = len(Set)
print partition(Set,n)


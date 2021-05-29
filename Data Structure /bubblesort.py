def outerloop(l,i,n):
  if i >=n-1 :
    print l 
    return 0
 
  else : 
   j = 0
   innerloop(l,i,j,n)
   i = i+1
   outerloop(l,i,n)


def innerloop(l,i,j,n):
  if j >= n-1-i: 
    return 0 
  elif l[j] > l[j+1] :
    temp=l[j]
    l[j] = l[j+1]
    l[j+1] = temp   
  j= j+1
  innerloop(l,i,j,n) 



List = [1,33,4,2,5,77,7]
n = len(List)
outerloop(List,0,n)

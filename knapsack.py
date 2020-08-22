def Max(a,b):
  if a > b :
    return a
  else:
    return b  


def function(wt,value,w,n) :
    if w ==0  or n==0 :
        return 0 
    elif wt[n-1] <=w :
        return Max(value[n-1] + function(wt,value,w-wt[n-1],n-1),function(wt,value,w,n-1))
    elif wt[n-1] > w :
        return function(wt,value,w,n-1)
        
        
wt = [4,7,1,5]
value =[10,5,20,5]    
w=7
      
print function(wt,value,w,len(wt))           
       

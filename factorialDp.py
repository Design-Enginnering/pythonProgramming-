

def factorialDp(n):
     ar = [1]*n
     ar[0] = 1
     for i in range(1,len(ar)):
        ar[i] = n*ar[i-1]
     print(ar[n-1])   
     
        

n=int(input())
factorialDp(n)

def lcs(x,y,n,m):
    if(n==0 or m==0):
        return "No"
    elif x[n-1] == y[m-1] :
        return  "Yes"
    else :
        return lcs(x,y,n-1,m) or lcs(x,y,n,m-1)


x,y= [],[]
pair = int(input("How many pair of string\n"))
for i in range(pair):
    print(str(i+1) + "--> pair ")
    a = input("first string\n")
    x.append(a)
    b = input("second string \n")
    y.append(b)
   
for i in range(pair):    
    print(lcs(x[i],y[i],len(x[i]),len(y[i])))

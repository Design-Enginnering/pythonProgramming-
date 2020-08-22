def isValid(arr,i,j,visit):
    rows,col = len(arr),len(arr)
    if(i>=0 and j>=0 and i<rows and j<col  and arr[i][j] == 1 and visit[i][j] == 0):
      return  True
    return False


def shortest_path(arr,i,j,x,y,visit,dist,min_dist):
    #if(not isvalid(arr,i,j,visit)):
     #   return 1000
    if(x==i and y==j):
       return min(dist,min_dist)
    visit[i][j] = 1
    if(isValid(arr,i-1,j,visit)):
       min_dist = shortest_path(arr,i-1,j,x,y,visit,dist+1,min_dist)
    if(isValid(arr,i+1,j,visit)):
       min_dist = shortest_path(arr,i+1,j,x,y,visit,dist+1,min_dist)
    if(isValid(arr,i,j+1,visit)):
       min_dist = shortest_path(arr,i,j+1,x,y,visit,dist+1,min_dist)
    if(isValid(arr,i,j-1,visit)):
       min_dist = shortest_path(arr,i,j-1,x,y,visit,dist+1,min_dist)
 
    #left = shortest_path(arr,i,j-1,x,y,visit)+1
    #bottom = shortest_path(arr,i+1,j,x,y,visit)+1
    #right = shortest_path(arr,i,j+i,x,y,visit)+1
    #top=shortest_path(arr,i-1,j,x,y,visit)+1
    visit[i][j]= 0 
    #return max(max(left,bottom),max(right,top))   
    return min_dist   

arr = [[1,1,1,1,1],
       [1,1,0,0,1],
       [1,1,1,1,0],
       [0,0,0,1,1],
       [1,0,0,0,1]]
boolean =[[0]*len(arr)]*len(arr)    
min_dist = shortest_path(arr,0,0,0,4,boolean,0,float('inf'))
if(min_dist>=float('inf')):
   print("path can't find" )
else :
    print("path is find\n",min_dist)   
print(float('inf'))   

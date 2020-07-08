# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:00:21 2020

@author: Pooja
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:00:21 2020

@author: Pooja
"""

ls = []
start = []
print("\n Enter the start state of the puzzle:")
for j in range(0,3):
    ls=[]
    for i in range(0,3):
        ls.append(int(input()))
    start.append(ls)

bad = [[99,99,99],[99,99,99],[99,99,99]]

ls1 = []
goal = []
print("\n Enter the goal state of the  puzzle:")
for j in range(0,3):
    ls1=[]
    for i in range(0,3):
        ls1.append(int(input()))
    goal.append(ls1)
   
print("\n Start State is:\n",start)
print("\n End State is:\n",goal)

       

def calcu(mat,goal):
    temp2 = 0
    for i in range(3):
        for j in range(3):
            if(mat[i][j]!=goal[i][j]):
                temp2+=1
        
    #print("\n cost",temp2,"\n")
    return temp2

def copy(mat):
        temp = []
        for i in mat:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
   
def swaptop(mat):
    r=0
    c=0
    t=0
    temp = copy(mat)
    for i in range(3):
        for j in range(3):
            if(temp[i][j]==0):
                r=i
                c=j
                break
    if((r-1)<0):
        return bad
    else:
        t = temp[r][c]
        temp[r][c]=temp[r-1][c]
        temp[r-1][c]=t
        return temp

def swapleft(mat):
    r=0
    c=0
    t=0
    temp = copy(mat)
    for i in range(3):
        for j in range(3):
            if(temp[i][j]==0):
                r=i
                c=j
                break
    if((c-1)<0):
        return bad
    else:
        t = temp[r][c]
        temp[r][c]=temp[r][c-1]
        temp[r][c-1]=t
        return temp
   
def swapright(mat):
    r=0
    c=0
    t=0
    temp = copy(mat)
    for i in range(3):
        for j in range(3):
            if(temp[i][j]==0):
                r=i
                c=j
                break
    if((c+1)>2):
        return bad
    else:
        t = temp[r][c]
        temp[r][c]=temp[r][c+1]
        temp[r][c+1]=t
        return temp

def swapdown(mat):
    r=0
    c=0
    t=0
    temp = copy(mat)
    for i in range(3):
        for j in range(3):
            if(temp[i][j]==0):
                r=i
                c=j
                break
    if((r+1)>2):
        return bad
    else:
        t = temp[r][c]
        temp[r][c]=temp[r+1][c]
        temp[r+1][c]=t
        return temp
   

               
               
               
   
   
neu = 0   
heu = calcu(start,goal)
level = 0


mat1 = copy(start)
prev = 0
k=0

while(heu!=0):
#for i in range(3):
    a=calcu(swapdown(mat1),goal)
    b=calcu(swaptop(mat1),goal)
    c=calcu(swapleft(mat1),goal)
    d=calcu(swapright(mat1),goal)
    
    
    heu = min([a,b,c,d])
    #print("heu",heu)
    if(heu == calcu(swapdown(mat1),goal)):
        mat1 = copy(swapdown(mat1))
        print(mat1,"\n swapdown")
    elif(heu == calcu(swapright(mat1),goal)):
        mat1 = copy(swapright(mat1))
        print(mat1,"\n swapright")
    elif(heu == calcu(swaptop(mat1),goal)):
        mat1 = copy(swaptop(mat1))
        print(mat1,"\n swaptop")
    elif(heu == calcu(swapleft(mat1),goal)):
        mat1 = copy(swapleft(mat1))
        print(mat1,"\n swapleft")
                

    print("\n")
if(heu == 0):
    print("\n The final state has been reached!\n" ,mat1)
    
''' Output : 
    
 Enter the start state of the puzzle:

1

0

3

8

2

4

6

7

5

 Enter the goal state of the  puzzle:

8

1

3

0

2

4

6

7

5

 Start State is:
 [[1, 0, 3], [8, 2, 4], [6, 7, 5]]

 End State is:
 [[8, 1, 3], [0, 2, 4], [6, 7, 5]]
[[0, 1, 3], [8, 2, 4], [6, 7, 5]] 
 swapleft


[[8, 1, 3], [0, 2, 4], [6, 7, 5]] 
 swapdown



 The final state has been reached!
 [[8, 1, 3], [0, 2, 4], [6, 7, 5]]
 
 '''

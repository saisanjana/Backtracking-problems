def isSafe(x,y,sud,k):
    for i in range(9):
        if(sud[x][i]==k):
            return 0
    for i in range(9):
        if(sud[i][y]==k):
            return 0
    if(x>=0 and x<=2 and y>=0 and y<=2):
        for i in range(0,3):
            for j in range(0,3):
                if(sud[i][j]==k):
                    return 0
    elif(x>=3 and x<=5 and y>=0 and y<=2):
        for i in range(3,6):
            for j in range(0,3):
                if(sud[i][j]==k):
                    return 0
    elif(x>=6 and x<=8 and y>=0 and y<=2):
        for i in range(6,9):
            for j in range(0,3):
                if(sud[i][j]==k):
                    return 0
    elif(x>=0 and x<=2 and y>=3 and y<=5):
        for i in range(0,3):
            for j in range(3,6):
                if(sud[i][j]==k):
                    return 0
    elif(x>=3 and x<=5 and y>=3 and y<=5):
        for i in range(3,6):
            for j in range(3,6):
                if(sud[i][j]==k):
                    return 0
    elif(x>=6 and x<=8 and y>=3 and y<=5):
        for i in range(6,9):
            for j in range(3,6):
                if(sud[i][j]==k):
                    return 0
    elif(x>=0 and x<=2 and y>=6 and y<=8):
        for i in range(0,3):
            for j in range(6,9):
                if(sud[i][j]==k):
                    return 0
    elif(x>=3 and x<=5 and y>=6 and y<=8):
        for i in range(3,6):
            for j in range(6,9):
                if(sud[i][j]==k):
                    return 0
    elif(x>=6 and x<=8 and y>=6 and y<=8):
        for i in range(6,9):
            for j in range(6,9):
                if(sud[i][j]==k):
                    return 0
    return 1
    
def sudoku(x,y,sud):
    if(x==9):
        return 1
    if(sud[x][y]==0):
        for i in range(1,10):
            if(isSafe(x,y,sud,i)==1):
                sud[x][y]=i
                if(y==8):
                    if(sudoku(x+1,0,sud)==1):
                        return 1
                    else:
                        sud[x][y]=0
                else:
                    if(sudoku(x,y+1,sud)==1):
                        return 1
                    else:
                        sud[x][y]=0
        return 0
    else:
        if(y==8):
            if(sudoku(x+1,0,sud)==1):
                return 1
            else:
                return 0
        else:
            if(sudoku(x,y+1,sud)==1):
                return 1
            else:
                return 0
        
    
n=int(input()) #taking number of test cases
while(n>0):
    n=n-1
    sud=[]
    l=input().split() #reading an unsolved sudoku
    k=0
    for i in range(9):
        mat=[0 for j in range(9)]
        sud.append(mat)
    for i in range(9):
        for j in range(9):
            sud[i][j]=int(l[k])
            k=k+1
    if(sudoku(0,0,sud)):
        k=0
        for i in range(9):
            for j in range(9):
                l[k]=sud[i][j]
                k=k+1
        for i in range(81):
            print(l[i],end=" ")
        print()
            
    

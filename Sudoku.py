if __name__ == "__main__":
    n = 5
    arr = [[None for i in range(n)] for j in range(n)]
    print(arr)
    arr[0][2] = 1
    row = 0
    col = 2
    print(arr)
    for i in range(2,n*n+1):
        if(row>0 and col>0):
            if(arr[row-1][col-1]==None):
                arr[row-1][col-1] = i
                row = row-1
                col = col-1
            elif(row==(n-1)):
                row = 0
                arr[row][col] = i
            else:
                arr[row+1][col] = i
                row = row+1
        elif(row==0 and col==0):
                if(arr[n-1][n-1]==None):
                    arr[n-1][n-1] = i
                    row = n-1
                    col = n-1 
                else:
                    arr[1][0] = i
                    row = 1
                    col = 0
        elif(row==0 and col>0):
                    if(arr[n-1][col-1]==None):
                        arr[n-1][col-1] = i
                        row = n-1
                        col = col-1
                    else:
                        arr[1][col] = i
                        row = 1
        elif(row>0 and col==0):
                    if(arr[row-1][n-1]==None):
                        arr[row-1][n-1] = i
                        row = row-1
                        col = n-1
                    elif(row == (n-1)):
                        arr[0][col] = i
                        row = 0
                    else:
                        arr[row+1][col] = i
                        row = row+1

    print(arr)




if __name__ == "__main__":
    n = int(input("Enter Number of items : "))
    profit = [None for i in range(n+1)]
    weight = [None for i in range(n+1)]

    print("Enter profits : ", end="")
    for i in range(1, n+1):
        profit[i] = int(input())
    print("Enter Weights : ", end="")
    for i in range(1, n+1):
        weight[i] = int(input())

    m = int(input("Enter Container Size : "))

    k = [[None for i in range(9)] for j in range(5)]

    for i in range(n+1):
        for w in range(m+1):
            if(i == 0 or w == 0):
                k[i][w] = 0
            elif(weight[i] <= w):
                k[i][w] = max((profit[i]+k[i-1][w-weight[i]]), k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    print(f"Start from : {k[n][w]}")
    # print(k)
    # Calculate objects which are included
    print("Items Which are included : ")
    i = n
    j = m
    while(i > 0 and j >= 0):
        if(k[i][j] == k[i-1][j]):
            print(f"item - {i} = 0")
            i -= 1
        else:
            print(f"item - {i} = 1")
            j = j-weight[i]
            i -= 1


def knapsack(n,wl,vl,W) :
    matrix = [[-1 for x in range(W+1)] for x in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,W+1):
            if (i==0) or (j==0):
                matrix[i][j] = 0
            elif (j<wl[i-1]) and (i>0) : matrix[i][j] = matrix[i-1][j]
            else : matrix[i][j] = max(matrix[i-1][j],matrix[i-1][j-wl[i-1]]+vl[i-1])
    stop=False
    i=n
    j=W
    list_pris=[]
    while (stop==False):
        if (matrix[i][j]!=matrix[i-1][j]):
            list_pris.append(i)
            i -= 1
            j -= wl[i]
        else :
            i -= 1
        if (i==0) : stop = True
    return matrix[n][W],list_pris
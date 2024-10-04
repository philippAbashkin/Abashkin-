a = 'aas'
b = 'asdasd'
def levenstein(a,b):
    len_a = len(a)
    len_b = len(b)
    res = [[-1 for i in range(len_b+1)] for j in range(len_a+1)] #задаем двумерную матрицу
    #print(res)
    k = 0
    for i in range(len_b+1): # заполняем первую строчку
        res[0][i] = k
        k += 1
    k = 0
    for i in range(len_a+1): # заполняем первый столбец
        res[i][0] = k
        k += 1
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            #print(i,j)
            if a[i-1] == b[j-1]:
                res[i][j] = min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1])
            else:
                res[i][j] = min(res[i - 1][j] + 1, res[i][j - 1] + 1, res[i - 1][j - 1] + 1)
    #for s in res:
    #    print(s)
    return res[-1][-1]
print(levenstein('aabaaa','aabaaa'))

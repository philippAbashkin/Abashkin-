#6 Напишите функцию, считающую коэффициенты МНК для набора измерений x и y.
import numpy as np
x = np.array([3,6,7,8,5,6,4])
y = np.array([7,3,9,2,6,4,7])
a = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) * np.mean(x)**2)
b = np.mean(y) - a*np.mean(x)
std_a = 1/np.sqrt(len(x)) * np.sqrt((np.mean(y**2)-np.mean(y)**2)/((np.mean(x**2)-np.mean(x)**2))-a**2)
str_b = std_a* np.sqrt(np.mean(x**2)-np.mean(x)**2)
print(std_a, str_b)



#5
# n, m = [int(i) for i in input().split()]
# matrix = []
# for i in range(n):
#     temp = [0 for num in range(m)]
#     matrix.append(temp)
# x,y,= 0, 0
# k = int(1)
# matrix[0][0]=1
# while k < m*n:
#     if x + 1 < m:
#         if matrix[y][x+1] == 0:
#             x+=1
#             k+=1
#             matrix[y][x] = k
#             continue
#     if y+1< n:
#         if matrix[y+1][x] == 0:
#             y+=1
#             k+=1
#             matrix[y][x] = k
#             continue
#     if matrix[y][x-1] == 0 and x-1>=0:
#         x-=1
#         k+=1
#         matrix[y][x] = k
#         continue
#     while matrix[y-1][x] == 0:
#         y-=1
#         k+=1
#         matrix[y][x] = k
#
# for row in matrix:
#     print(*row)

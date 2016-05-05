# -*- coding:utf-8 -*-

array1 = [ i for j in range(3) for i in range(5)]
print(array1)

array2 = [j for j in range(3) for i in range(5)]
print(array2)

print()
matrix = [[row for col in range(5)] for row in range(5)]
for row in matrix:
    print(row)
# 矩阵翻转
print('矩阵翻转'.center(50, '-'))
inverse_matrix = [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[1]))]
for row in inverse_matrix:
    print(row)

# 下面的方法在一个矩阵原地翻转,只适用于方块阵
print('下面的方法在一个矩阵原地翻转,只适用于方块阵')
array=[[col for col in range(5)] for row in range(5)] #初始化一个4*4数组

for row in array: #旋转前先看看数组长啥样
    print(row)

print('-------------')
for i,row in enumerate(array):

    for index in range(i,len(row)):
        tmp = array[index][i]  # get each rows' data by column's index
        array[index][i] = array[i][index]
        print(tmp, array[i][index])  # = tmp
        array[i][index] = tmp
    for r in array:
        print(r)
    print('--one big loop --')
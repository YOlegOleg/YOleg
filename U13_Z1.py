import random

def pr(t):
    for i in t:
        print (*i)
        
x=int(input('The width of the matrix x='))
y=int(input('The height of the matrix y='))
# Интервал случайных чисел в от -200 до 200
mat_1 =[[random.randint(-200, 200) for i in range(x)] for i in range(y)]
mat_2 =[[random.randint(-200, 200) for i in range(x)] for i in range(y)]
mat_s =[[0 for i in range(x)] for i in range(y)]

for i in range(y):
    for j in range(x):
        mat_s[i][j]=mat_1[i][j]+mat_2[i][j]

print('Matrix No. 1')
pr(mat_1)
print('Matrix No. 2')
pr(mat_2)
print('The sum of the matrices:')
pr(mat_s)

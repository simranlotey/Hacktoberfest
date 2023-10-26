# MOHD FAIZ ASLAM             
# ------------Gauss Elimination with Pivoting-----------
import numpy as np
from numpy import array,zeros,linalg,fabs

# taking user input for nXn matrix
n_n = int(input("Enter the number of row x col: "))

# taking element for the matrix
print("Enter nine numbers separated by space")
val = list(map(int, input().split()))
a_mat = np.array(val).reshape(n_n,n_n)

a = np.floor(a_mat) # coefficient matrix

b = array([5,7,2],float)

n = len(b)
x = zeros(n,float) # variable matrix initialised with 0

# Here we have used the linalg function of numpy, which will give us the output. 
# So we check with our program, whether out program gives expected result or not
print("Let's check the output with Linear Algebra module: ")
print(linalg.solve(a,b))

# Elimination process
for k in range(n-1):
    if fabs(a[k,k]) < 1.0e-12:
        for i in range(k+1,n):
            if fabs (a[i,k] > fabs(a[k,k])):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
                break
    for i in range(k+1,n):
        if a[i,k] == 0:
            continue
        fctr = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - fctr*a[i,j]
        b[i] = b[k] - fctr*b[i]

# Back subsitution process
x[n-1] = b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum = 0
    for j in range(i+1,n):
        sum = sum + a[i,j]*x[j]
    x[i] = (b[i] - sum)/a[i,i]


# Outcome through out program
print("The Solution vector is: ")
print(x)

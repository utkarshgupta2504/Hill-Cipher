#!/usr/bin/env python
# coding: utf-8

# # Defining Functions

# In[58]:


from random import random as rand    #For generatig random numbers (used in key)

def det_nxn(mat, n): #Determinant of nxn matrix (Using recursion)
    
    if n == 1:
        
        return mat[0][0]
    
    elif n == 2:
        
        return (mat[0][0] * mat[1][1]) - (mat[0][1]*mat[1][0])
    
    else:
        
        ans = 0

        for j in range(n): 
            
            cofactor = []

            for k in range(n):
                
                temp = []

                for l in range(n):

                    if k != 0 and l != j:
                        
                        temp.append(mat[k][l])
                                   
                if temp:
                    cofactor.append(temp)
                
            ans += mat[0][j] * det_nxn(cofactor, n-1) * ((-1)**j)
            
        return ans

    
def transpose_matrix(mat, n):  #Transpose of a matrix
    
    matrix = []
    
    for i in range(n):
        
        temp = []
        
        for j in range(n):
            
            temp.append(mat[j][i])
            
        matrix.append(temp)
        
    return matrix
    

def adj_nxn(mat, n): #Adjoint of a nxn matrix
    
    adj_matrix = []
    
    for i in range(n):
        
        temprow = []
        
        for j in range(n):
            
            cofactor = []

            for k in range(n):
                
                temp = []

                for l in range(n):

                    if k != i and l != j:
                        
                        temp.append(mat[k][l])
                                   
                if temp:
                    cofactor.append(temp)
                
            temprow.append(det_nxn(cofactor, n-1) * ((-1)**(i+j)))
            
        adj_matrix.append(temprow)
            
    return transpose_matrix(adj_matrix, n)
    
                
def multiply_matrix(m1, r1, c1, m2):  #Multiplying Matrices
    
    mult = []
    
    for i in range(r1):
        
        temp = []
        
        for j in range(c1):
            
            sum = 0
            
            for k in range(c1):
                
                sum += m1[i][k]*m2[k][j]
                
            temp.append(sum)
    
        mult.append(temp)
    
    return mult

def inverseMod(a, m) :  #Inverse Mod Function
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

alphas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.')  #List for storing all the letters in order


# # Converting Plain Text to Cipher Text

# In[59]:


plainText = input("Enter Plain Text: ")
keyn = int(input("Enter order of key matrix: "))

plainTextMatrix = [[plainText[i:i+keyn]] for i in range(0, len(plainText), keyn)]  #Dividing plain text in grps of 3

plainTextMatrix[-1][-1] = plainTextMatrix[-1][-1] + ' '*(keyn - len(plainText)%keyn)  #Adding blank spaces if last < 3

key = [[int(rand() * 100000000) % 10 for i in range(keyn)] for i in range(keyn)]  #Generating random key matrix

det_key = det_nxn(key, keyn)

print("Generated Key:", key)

while(det_key % 29 == 0 or 29%det_key == 0):    
    key = [[int(rand() * 100000000) % 10 for i in range(keyn)] for i in range(keyn)]   #Check if gcd(key, 29) == 1
    det_key = det_nxn(key, keyn) 
    
plainTextMatrixNum = []
    
for i in plainTextMatrix:
    
    plainTextMatrixNum.append(list(map(lambda x: alphas.index(x), list(i[0]))))  #Converting text to numbers
    
cipherTextMatrixNum = multiply_matrix(plainTextMatrixNum, len(plainTextMatrixNum), keyn, key)  #Getting cipher text Matrix

cipherTextMatrix = []

for i in cipherTextMatrixNum:
    
    cipherTextMatrix.append(list(map(lambda x: alphas[x%29], i)))   #Converting numbers to text
    
cipherText = ''

for i in cipherTextMatrix:
    
    cipherText += ''.join(i)    #Getting the whole cipher text
    
print("Plain Text:", plainText)
print("Cipher:", cipherText)


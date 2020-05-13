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


cipherText = input("Enter Cipher Text: ")

keynum = list(map(int, input("Enter Key(Seperated by spaces): ").split()))
keyn = int(len(keynum)**(1.0/2))

key = [keynum[i:i+keyn]for i in range(0, len(keynum), keyn)]

cipherTextMatrix = [[cipherText[i:i+keyn]] for i in range(0, len(cipherText), keyn)]

cipherTextMatrixNum = []
    
for i in cipherTextMatrix:
    
    cipherTextMatrixNum.append(list(map(lambda x: alphas.index(x), list(i[0]))))


# # Operations on key to find inverse

# In[61]:


det_key = det_nxn(key, keyn)

invmod = inverseMod(det_key%29, 29)

adjKey = adj_nxn(key, keyn)

invKey = []

for i in adjKey:
    
    invKey.append(list(map(lambda x: (invmod*(x%29))%29, i)))
    
print("Inverse Key:",invKey)


# # Generating Plain text using inverse key

# In[62]:


plainTextMatrixNum = multiply_matrix(cipherTextMatrixNum, len(cipherTextMatrixNum), keyn, invKey)

plainTextMatrix = []

for i in plainTextMatrixNum:
    
    plainTextMatrix.append(list(map(lambda x: alphas[x%29], i)))
    
plainText = ''

for i in plainTextMatrix:
    
    plainText += ''.join(i)
    
print("Cipher Text:", cipherText)
print("Key:", key)
print("Plain Text:", plainText)
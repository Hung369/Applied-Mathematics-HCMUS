import numpy as np

def Gauss_Elimination(a):
    r, c = a.shape
    if r == 0 or c == 0:
        return a

    for i in range(len(a)):
        if a[i,0] != 0:
            break
        else:
            b = Gauss_Elimination(a[:,1:])
            return np.hstack([a[:,:1], b])

    if i > 0:
        ith_row = a[i].copy()
        a[i] = a[0]
        a[0] = ith_row

    a[0] = a[0] / a[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    a[1:] -= a[0] * a[1:,0:1]

    b = Gauss_Elimination(a[1:,1:])

    return np.vstack([a[:1], np.hstack([a[1:,:1], b]) ])



def Back_Substitution(x,a,n):
    if a[n - 1][n - 1] == 0:
        x[n - 1] = a[n - 1][n]
    else:
        x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1): # i goes n-2,n-3,...,2,1,0
        x[i] = a[i][n]

        for j in range(i + 1, n): # j goes i+1,i+2,...,n-2,n-1
            x[i] = x[i] - a[i][j] * x[j]

        if a[i][i] == 0:
            x[i] = 1
        else:
            x[i] = x[i] / a[i][i]

    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print("X"+str(i+1)+' = '+str(x[i]) ,end='\t')

def PrintMatrix(a):
    for i in a:
        for j in i:
            print(j, end=" ")
        print()

if __name__ == '__main__':
    n = int(input('Enter number of unknowns: '))
    a = np.zeros((n, n + 1))
    coef = np.zeros((n, n))
    x = np.zeros(n)

    # Reading augmented matrix coefficients
    print('Enter Augmented Matrix Coefficients:')
    for i in range(n):
        for j in range(n + 1):
            a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))
            if j in range(n):
                coef[i][j] = a[i][j]

    # check condition.
    rank_a = np.linalg.matrix_rank(a)
    rank_co = np.linalg.matrix_rank(coef)
    if rank_co < rank_a:
        print('Vo nghiem')
    elif rank_co == rank_a and rank_a == n:
        print('Co nghiem duy nhat')
        # Applying Gauss Elimination
        Gauss_Elimination(a)
        PrintMatrix(a)
        Back_Substitution(x,a,n)
    elif rank_co == rank_a and rank_a < n:
        print('Co vo so nghiem')
        Gauss_Elimination(a)
        PrintMatrix(a)
        Back_Substitution(x, a, n)

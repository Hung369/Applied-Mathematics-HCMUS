import numpy as np
import copy

def inverse(a):
    lead = 0  # cột của phần tử trụ khác 0
    row = len(a)
    column = row

    for r in range(row):
        if column <= lead:
            break

        i = r  # dòng của phần tử trụ khác 0
        while a[i][lead] == 0:
            i += 1
            if i == row:
                i = r
                lead += 1
                if lead == column:
                    break

        # đổi dòng i và r
        temp = copy.deepcopy(a[i])
        a[i] = copy.deepcopy(a[r])
        a[r] = copy.deepcopy(temp)

        a[r] /= a[r][lead]  # bắt đầu biến đổi Gauss-Jordan
        for k in range(row):
            if k != r:
                a[k] -= a[r] * a[k][lead]

        lead += 1

def Display(a, n):
    for i in range(n):
        for j in range(n, n + n):
            print(a[i][j], end=' ')
        print()


if __name__ == '__main__':
    n = int(input('Nhập kích thước ma trận vuông: '))
    a = np.zeros((n, n + n), dtype=float)
    A = np.zeros((n, n), dtype=float)

    # Reading augmented matrix coefficients
    print('Nhập các hệ số cho ma trận vuông:')
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input('A[' + str(i) + '][' + str(j) + ']='))
            a[i][j] = A[i][j]
            if i == j:
                a[i][j + n] = 1

    det_A = np.linalg.det(A)
    if det_A != 0:
        print('Ma trận khả nghịch')
        inverse(a)
        Display(a, n)
    else:
        print('Ma trận không khả nghịch')

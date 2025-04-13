# Matriks A dan B
Matriks_A = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [5, 5, 5, 5, 5]
]

Matriks_B = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

Matriks_C = []
for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += Matriks_A[i][k] * Matriks_B[k][j]
        baris.append(total)
    Matriks_C.append(baris)

# Tampilan Output
print("Matriks A:")
for row in Matriks_A:
    print(row)

print("\nMatriks B:")
for row in Matriks_B:
    print(row)

print("\nHasil A x B:")
for row in Matriks_C:
    print(row)

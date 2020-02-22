number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

print(number_grid[0][0])  ## Will print the o row and o coloumn value in the grid.
# =====================
# OUTPUT:
# 1
# =====================

for row in number_grid:
    print(row)
# =========================
# OUTPUT:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [0]
# =========================
for coloumn in number_grid:
    print(coloumn)
# ===========================
# OUTPUT:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [0]
# ===========================

for row in number_grid:
    for coloumn in row:
        print(coloumn)
# =============================
# OUTPUT:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# ============================
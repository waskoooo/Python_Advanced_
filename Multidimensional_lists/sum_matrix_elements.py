row, cow = [int(el) for el in input().split(', ')]

total_amount = 0
matrix = []
for i in range(row):
    row_data = [int(el) for el in input().split(', ')]
    total_amount += sum(row_data)
    matrix.append(row_data)

print(total_amount)
print(matrix)


row = int(input())
# 1.type
# flatten = []

# for i in range(row):
#     row_data = [int(el) for el in input().split()]
#     flatten.extend(row_data)
# print(flatten)

# 2.type:
# flatten = []
# for row in matrix:
#     for el in row:
#         flatten.append(el)

# flatten = [el for row in matrix for el in row]
# 3.type

matrix = [map(int, input().split(', ')) for _ in range(row)]
flattened = [num for row in matrix for num in row]
print(flattened)

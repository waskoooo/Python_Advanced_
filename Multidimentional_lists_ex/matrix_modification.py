size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":
    type_command, r, c, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= r < size and 0 <= c < size):
        print("Invalid coordinates")
    elif command == "Add":
        matrix[r][c] += number
    elif command == "Subtract":
        matrix[r][c] -= number

    command = input().split()

[print(*row) for row in matrix]

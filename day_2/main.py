
with open("data.txt") as file:
    data = [line.strip() for line in file.readlines()]
    file.close()  

a = 'A'
b = 'B'
c = 'C'
d = 'D'
_ = None

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x = 1
y = 1

code = ''

for seq in data:
    for dir in seq:
        match dir:
            case 'U':
                if x > 0: x -= 1
            case 'R':
                if y < 2: y += 1
            case 'D':
                if x < 2: x += 1
            case 'L':
                if y > 0: y -= 1

    num = keypad[x][y]
    code += str(num)

print(f"Part 1: {code}")


# ===================================================== #

keypad = [
    [_, _, 1, _, _],
    [_, 2, 3, 4, _],
    [5, 6, 7, 8, 9],
    [_, a, b, c, _],
    [_, _, d, _, _]
]

x = 2
y = 0

code = ''

for seq in data:
    for dir in seq:
        match dir:
            case 'U':
                if x > 0: x -= 1

                if keypad[x][y] == None:
                    x += 1

            case 'R':
                if y < 4: y += 1

                if keypad[x][y] == None:
                    y -= 1

            case 'D':
                if x < 4: x += 1

                if keypad[x][y] == None:
                    x -= 1

            case 'L':
                if y > 0: y -= 1

                if keypad[x][y] == None:
                    y += 1

    num = keypad[x][y]
    code += str(num)

print(f"Part 2: {code}")
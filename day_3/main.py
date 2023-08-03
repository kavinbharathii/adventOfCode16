
with open("data.txt") as file:
    data = [str(line.strip()) for line in file.readlines()]
    file.close()

# possible_triangles = 0

# for n, triangle in enumerate(data):
#     sides = [int(i.strip()) for i in triangle.split("  ") if i.strip().isnumeric()]
    
#     a, b, c = sorted(sides)

#     if a + b > c:
#         possible_triangles += 1

# print(f"Part 1: {possible_triangles}")

possible_triangles = 0
sides = [str(int(i.strip())).zfill(3) for triangle in data for i in triangle.split("  ") if i.strip().isnumeric()]

col1 = []
col2 = []
col3 = []

for n, triangle in enumerate(data):
    sides = [int(i.strip()) for i in triangle.split("  ") if i.strip().isnumeric()]
    
    a, b, c = sides
    col1.append(a)
    col2.append(b)
    col3.append(c)

for i in range(0, len(col1), 3):
    a, b, c = sorted(col1[i:i + 3])

    if a + b > c:
        possible_triangles += 1

for i in range(0, len(col2), 3):
    a, b, c = sorted(col2[i:i + 3])

    if a + b > c:
        possible_triangles += 1

for i in range(0, len(col3), 3):
    a, b, c = sorted(col3[i:i + 3])

    if a + b > c:
        possible_triangles += 1

print(possible_triangles)
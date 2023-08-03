
with open("data.txt") as file:
    data = file.readline()
    file.close()    
    
sequence = data.split(", ")
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_facing_dir = 0                          # Facing north
current_position = [0, 0]
positions_visited = []
position_visited_twice = None

for seq in sequence:
    dir = seq[0]
    steps = int(seq[1:])

    match dir:
        case 'R':
            current_facing_dir += 1
        case 'L':
            current_facing_dir -= 1

    for _ in range(steps):
        current_position[0] += directions[current_facing_dir % 4][0] 
        current_position[1] += directions[current_facing_dir % 4][1]

        if (tuple(current_position) in positions_visited) and (position_visited_twice == None):
            position_visited_twice = tuple(current_position)
        
        positions_visited.append(tuple(current_position))

total_blocks_traversed = abs(current_position[0]) + abs(current_position[1])
total_blocks_to_hq = abs(position_visited_twice[0]) + abs(position_visited_twice[1])

print(f"Part 1: {total_blocks_traversed}")
print(f"Part 2: {total_blocks_to_hq}")

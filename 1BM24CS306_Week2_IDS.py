
def depth_limited_search(state, goal, limit, path, visited):
    if state == goal:
        return path

    if limit == 0:
        return None

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = []
    if row > 0:
        moves.append(zero - 3)
    if row < 2:
        moves.append(zero + 3)
    if col > 0:
        moves.append(zero - 1)
    if col < 2:
        moves.append(zero + 1)

    for move in moves:
        new_state = list(state)
        new_state[zero], new_state[move] = (
            new_state[move], new_state[zero]
        )
        new_state = tuple(new_state)

        if new_state not in visited:
            visited.add(new_state)
            result = depth_limited_search(
                new_state, goal, limit - 1,
                path + [new_state], visited
            )

            if result:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        visited = {start}
        result = depth_limited_search(
            start, goal, depth, [start], visited
        )

        if result:
            return result

        depth += 1


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path = ids(start, goal)

print("Solution found:")
for state in path:
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

print("Number of moves:", len(path) - 1)

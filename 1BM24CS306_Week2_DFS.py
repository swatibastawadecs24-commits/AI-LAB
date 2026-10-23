
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)
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
                stack.append((new_state, path + [new_state]))

    return None


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

path = dfs(start, goal)

if path:
    print("Solution found:")
    for state in path:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()

    print("Number of moves:", len(path) - 1)
else:
    print("No solution found")


import random

N = 4

def calculate_cost(board):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):
            
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                cost += 1

    return cost



def display_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()



def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if board[col] != row:
                neighbor = board.copy()
                neighbor[col] = row
                neighbors.append(neighbor)

    return neighbors


def hill_climbing():
    
    current = [random.randrange(N) for _ in range(N)]

    while True:
        current_cost = calculate_cost(current)

        print("\nCurrent state:", current)
        print("Current cost:", current_cost)
        display_board(current)

        if current_cost == 0:
            print("Goal state reached!")
            return

        neighbors = get_neighbors(current)

        
        best = min(neighbors, key=calculate_cost)
        best_cost = calculate_cost(best)

        print("\nBest neighbor:", best)
        print("Neighbor cost:", best_cost)

        
        if best_cost >= current_cost:
            print("Local minimum reached. Restarting...\n")
            current = [random.randrange(N) for _ in range(N)]
        else:
            current = best


hill_climbing()

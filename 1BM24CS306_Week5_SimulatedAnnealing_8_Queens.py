import random
import math

N = 8


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


def simulated_annealing():
    current = [random.randrange(N) for _ in range(N)]
    current_cost = calculate_cost(current)

    best = current.copy()
    best_cost = current_cost

    temperature = 100.0
    cooling_rate = 0.99
    min_temperature = 0.001
    iteration = 0

    while temperature > min_temperature:
        if current_cost == 0:
            break

        
        neighbor = current.copy()
        col = random.randrange(N)
        row = random.randrange(N - 1)

        
        if row >= neighbor[col]:
            row += 1

        neighbor[col] = row
        neighbor_cost = calculate_cost(neighbor)

        delta = neighbor_cost - current_cost

        
        if (delta < 0 or
            random.random() < math.exp(-delta / temperature)):
            current = neighbor
            current_cost = neighbor_cost

        
        if current_cost < best_cost:
            best = current.copy()
            best_cost = current_cost

        iteration += 1

        print(
            "Iteration:", iteration,
            "| Temperature:", round(temperature, 4),
            "| Current cost:", current_cost,
            "| Neighbor cost:", neighbor_cost,
            "| Best cost:", best_cost
        )

        
        temperature *= cooling_rate

    print("\nFinal best state:", best)
    print("Final minimum cost:", best_cost)
    print("Total iterations:", iteration)
    display_board(best)

    if best_cost == 0:
        print("Solution found!")
    else:
        print("No solution found in this run. Run again.")


simulated_annealing()
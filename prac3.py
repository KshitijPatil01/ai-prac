import heapq
#TC:b^d
# Calculate heuristic: number of misplaced tiles
def heuristic(state, goal):
    return sum(state[i] != 0 and state[i] != goal[i]
               for i in range(9))


# A* Search Algorithm
def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start, [start])]
    best_cost = {start: 0}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        # Check if goal is reached
        if state == goal:
            return path

        # Generate neighbouring states
        z = state.index(0)
        x, y = divmod(z, 3)

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny

                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)

                new_g = g + 1

                if new not in best_cost or new_g < best_cost[new]:
                    best_cost[new] = new_g
                    new_f = new_g + heuristic(new, goal)

                    heapq.heappush(
                        pq, (new_f, new_g, new, path + [new])
                    )

    return None


# Initial and goal states
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = astar(start, goal)

# Display solution
if result:
    for step, state in enumerate(result):
        print("Step", step)
        for i in range(0, 9, 3):
            print(' '.join(str(n) if n != 0 else '_'
                           for n in state[i:i+3]))
        print()

    print("Total moves:", len(result) - 1)
else:
    print("No solution found")

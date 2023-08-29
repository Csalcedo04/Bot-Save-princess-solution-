def displayPathtoPrincess(N, grid):
    # Find the positions of the bot and the princess
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_pos = (i, j)
            if grid[i][j] == 'p':
                princess_pos = (i, j)
    
    # Define possible moves
    moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
    
    # Initialize BFS queue with bot's position
    queue = [(bot_pos, [])]
    visited = set([bot_pos])
    
    while queue:
        current_pos, path = queue.pop(0)
        
        if current_pos == princess_pos:
            for move in path:
                print(move)
            return
        
        for move, direction in moves.items():
            new_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N and new_pos not in visited:
                queue.append((new_pos, path + [move]))
                visited.add(new_pos)

# Read input
N = int(input())
grid = [list(input().strip()) for _ in range(N)]

# Call the function
displayPathtoPrincess(N, grid)
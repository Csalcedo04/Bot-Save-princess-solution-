# Bot Save Princess solution, using BFS search
Bot Save Princess is a searching problem posed by hackerRank that challenges programmers to devise efficient algorithms to guide a bot through a grid to rescue a princess.  In this repository, we present our solution to this problem utilizing the ```Breadth-First Search (BFS)``` searching method with ```Python3```. Our solution aims to showcase the effectiveness of BFS in solving pathfinding problems within a grid-like environment.
## Table of Contents:
- [Implementation of the Proposed BFS Method](###Implementation-of-the-Proposed-BFS-Method)
- [System outputs](###Outputs-del-sistema)
- [Link](###Link)

### Implementation of the Proposed BFS Method
```
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
```
### System outputs:
![Imagen de WhatsApp 2023-08-28 a las 22 27 36](https://github.com/Csalcedo04/Bot-Save-princess-solution-/assets/98894266/6ad584a5-34df-439e-8540-f532653414dc)

### Link
- HackerRank challenge: [Add solution URL here](https://www.hackerrank.com/challenges/saveprincess/problem)

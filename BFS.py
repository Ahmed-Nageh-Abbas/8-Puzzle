from collections import deque

def generate_moves(state):
    # Generate possible moves (up, down, left, right)
    moves = []
    i = state.index(0)
    if i % 3 > 0: moves.append(('left', i, i-1))
    if i % 3 < 2: moves.append(('right', i, i+1))
    if i // 3 > 0: moves.append(('up', i, i-3))
    if i // 3 < 2: moves.append(('down', i, i+3))
    return moves

def apply_move(state, move):
    # Apply a move to the state
    state = list(state)
    state[move[1]], state[move[2]] = state[move[2]], state[move[1]]
    return tuple(state)

def bfs(initial_state, goal):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        visited.add(state)
        for move in generate_moves(state):
            next_state = apply_move(state, move)
            if next_state not in visited:
                queue.append((next_state, path + [state]))

    return None

#print(bfs((5,6,7,4,0,8,3,2,1), (1,3,4,8,6,2,7,0,5)))       
"""
5 6 7
4 0 8
3 2 1
1 3 4
8 6 2
7 0 5
"""
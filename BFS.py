from copy import *
from collections import deque

ar = [ 0,0,1,-1 ]
ac = [ 1,-1,0,0 ]
def valid(i, j):
    return i >= 0 and i <= 2 and j >= 0 and j <= 2

def tpl(lst_of_lsts):
    return tuple(tuple(lst) for lst in lst_of_lsts)

def bfs(start, x, y, end):
    parent = {}

    visited = set()
    visited.add(str(start))
    
    qu = deque([([], start, x, y)])
    
    while qu:
        front = qu.popleft()
        cur_parent = front[0]
        cur_state = front[1]
        cur_x = front[2]
        cur_y = front[3]

        parent[tpl(cur_state)] = tpl(cur_parent)
        if cur_state == end: break
        
        New_state = deepcopy(cur_state) #remember copy
        for k in range(4):
            ii = cur_x + ar[k]
            jj = cur_y + ac[k]
            if valid(ii, jj):
                New_state[cur_x][cur_y], New_state[ii][jj] = New_state[ii][jj], New_state[cur_x][cur_y]
                
                if str(New_state) not in visited:
                    visited.add(str(New_state))
                    qu.append((cur_state, deepcopy(New_state), ii, jj))
                    
                New_state[cur_x][cur_y], New_state[ii][jj] = New_state[ii][jj], New_state[cur_x][cur_y]
    return parent            
"""
5 6 7
4 0 8
3 2 1
1 3 4
8 6 2
7 0 5
"""
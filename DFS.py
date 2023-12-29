from copy import *
from collections import deque
import sys
sys.setrecursionlimit(100000)
def lists(lst):
    lsts, row = [], []
    for i in range(10):
        if i % 3 == 0 and i:
            lsts.append(deepcopy(row))
            if i < 9: row = [lst[i]]
            else: row = []
        else: row.append(lst[i])
    return lsts
graph={
    0:(1,3),
    1:(0,2,4),
    2:(1,5),
    3:(0,4,6),
    4:(1,3,5,7),
    5:(2,4,8),
    6:(3,7),
    7:(4,6,8),
    8:(5,7)
}
visited = set()
def dfs(cur, x, end, path=[]):
    if cur==end:
        path.append(lists(end))
        return True
    if str(cur) in visited:
        return False
    
    visited.add(str(cur))
    for nx in graph[x]:
        cur[x],cur[nx]=cur[nx],cur[x]
        solution=dfs(cur,nx,end,path)
        cur[x],cur[nx]=cur[nx],cur[x]
        if solution:
            path.append(lists(cur))
            return True
    return False
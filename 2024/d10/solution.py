import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732


def process_input(filename):
    # read 2d array
    with open(filename, 'r') as file:
        # convert to int if necessary
        return [[int(c) for c in line.strip()] for line in file if line.strip()]
    

def p1(filename):
    grid = process_input(filename)
    
    m, n = len(grid), len(grid[0])
    visited = set()
    tailheads = collections.defaultdict(set)
    
    
    def dfs(x, y):
        if (x, y) in visited:
            return
        visited.add((x, y))
        if grid[x][y] == 9:
            tailheads[(x, y)].add((x, y))
            return
        # use nx, ny
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y] + 1:
                dfs(nx, ny)
                tailheads[(x, y)].update(tailheads[(nx, ny)])
        
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                starts.append((i, j))
    
    res = 0
    for start in starts:
        dfs(*start)
    
    for start in starts:
        res += len(tailheads[start])
    
    print(res)
    return res

print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)


def p2(filename):
    grid = process_input(filename)
    
    m, n = len(grid), len(grid[0])
    
    @functools.cache
    def dfs(x, y):
        if grid[x][y] == 9:
            return 1
        # use nx, ny
        paths = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y] + 1:
                paths += dfs(nx, ny)
        return paths
        
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                starts.append((i, j))
    
    res = 0
    for start in starts:
        res += dfs(*start)
    
    print(res)
    return res

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
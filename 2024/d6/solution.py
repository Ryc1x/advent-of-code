import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

rev_dirs = {
    (-1, 0): '^',
    (0, 1): '>',
    (1, 0): 'v',
    (0, -1): '<'
}

def pretty_print(grid, x, y, dx, dy):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == x and j == y:
                print(rev_dirs[(dx, dy)], end='')
            else:
                print('.' if grid[i][j] == 0 else '#', end='')
        print()
    input()

def process_input(filename):
    with open(filename) as file:
        # read input as 2d array
        matrix = [list(line.strip()) for line in file]
        grid = [list(line) for line in matrix]
        
        dir = None
        x, y = 0, 0
        # mark . as 0, # as 1, ^ as 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if matrix[i][j] == '.':
                    grid[i][j] = 0
                elif matrix[i][j] == '#':
                    grid[i][j] = 1
                elif grid[i][j] in dirs.keys():
                    dir = dirs[grid[i][j]]
                    grid[i][j] = 0
                    x, y = i, j
        
    return grid, dir, x, y


def p1(filename):
    grid, dir, x, y = process_input(filename)
    
    m, n = len(grid), len(grid[0])
    visited = [[0] * n for _ in range(m)]
    # move the robot in the direction of dir
    # if it hits a wall, turn right, until it goes out of the grid
    while x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
        # pretty_print(grid, x, y, dir[0], dir[1])
        # mark the current cell as visited
        visited[x][y] = 1
        nx, ny = x + dir[0], y + dir[1]
        # if outside the grid, end the loop
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            break
        # if the next cell is a wall, turn right
        if grid[nx][ny] == 1:
            dir = (dir[1], -dir[0])
        else:
            x, y = nx, ny
    
    res = sum(sum(row) for row in visited)
    print(res)
    
    return res, visited 
    
print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)

# we can allow removing one element from the array
def check_loop(grid, x, y, dir, obs=None):
    # check if adding obstacle at obs_x, obs_y will cause the robot to loop
    m, n = len(grid), len(grid[0])
    visited = [[0] * n for _ in range(m)]
    if obs:
        grid[obs[0]][obs[1]] = 1
    # move the robot in the direction of dir
    # if it hits a wall, turn right, until it goes out of the grid
    step = 0
    while True:
        # pretty_print(grid, x, y, dir[0], dir[1])
        # mark the current cell as visited
        if visited[x][y] > 4:
            # restore the grid
            if obs:
                grid[obs[0]][obs[1]] = 0
            return True
        visited[x][y] += 1
        nx, ny = x + dir[0], y + dir[1]
        # if outside the grid, end the loop
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            break
        # if the next cell is a wall, turn right
        if grid[nx][ny] == 1:
            dir = (dir[1], -dir[0])
        else:
            x, y = nx, ny
        step += 1
    # restore the grid
    if obs:
        grid[obs[0]][obs[1]] = 0
    return False
    
    
def p2(filename):
    grid, dir, x, y = process_input(filename)
    
    res, visited = p1(filename)
    
    res = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and visited[i][j] == 1:
                # try adding an obstacle at i, j
                if check_loop(grid, x, y, dir, (i, j)):
                    res += 1
            # print('checking for', i, ',' , j, 'res:', res)
            # print('remaining cells:', m * n - i * n - j)
    print(res)
    return res 

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
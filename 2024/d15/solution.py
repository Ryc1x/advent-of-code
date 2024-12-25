import math, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# https://adventofcode.com/2024/day/15

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

# <^^>>>vv<v>>v<<

# @ - robot
# # - wall
# . - empty space
# O - box, can be pushed

def process_input(filename):
    with open(filename, 'r') as file:
        # read as 2d array and a list of commands
        # split by \n\n
        grid, command = file.read().split('\n\n')
        grid = [list(r) for r in grid.split('\n')]
        command = command.replace('\n', '')
        
        # print(grid)
        # print(command)
        return grid, command
        

def pretty_print(grid):
    for row in grid:
        print(''.join(row))
    print()
    input()

dirmap = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

def move(grid, x, y, dx, dy):
    # if the next cell is a wall return the current position
    if grid[y + dy][x + dx] == '#':
        return x, y
    if grid[y + dy][x + dx] == 'O':
        # if the next cell is a box, check in that direction until it's not a box
        i = 1
        while grid[y + i * dy][x + i * dx] == 'O':
            i += 1
        if grid[y + i * dy][x + i * dx] == '#':
            return x, y
        else:
            grid[y + i * dy][x + i * dx] = 'O'
    # move the robot
    grid[y + dy][x + dx] = '@'
    grid[y][x] = '.'
    return x + dx, y + dy

def score(grid):
    # calculate the score of the grid
    # score = 100 * y + x for each box
    score = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[y][x] == 'O':
                score += 100 * y + x
    return score

def p1(filename):
    grid, command = process_input(filename)
    # simulate the game
    
    # find the starting position of the robot
    x, y = 0, 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                x, y = j, i
                break
    
    for c in command:
        dx, dy = dirmap[c]
        x, y = move(grid, x, y, dx, dy)
        # pretty_print(grid)
    
    print(score(grid))
    return score(grid)
    
    
print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)


# If the tile is #, the new map contains ## instead.
# If the tile is O, the new map contains [] instead.
# If the tile is ., the new map contains .. instead.
# If the tile is @, the new map contains @. instead.

def transform_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == '#':
                new_row.extend(['#', '#'])
            elif cell == 'O':
                new_row.extend(['[', ']'])
            elif cell == '.':
                new_row.extend(['.', '.'])
            elif cell == '@':
                new_row.extend(['@', '.'])
        new_grid.append(new_row)
    return new_grid

def move2(grid, x, y, dx, dy):
    # if the next cell is a wall return the current position
    if grid[y + dy][x + dx] == '#':
        return x, y
    if grid[y + dy][x + dx] in '[]':
        # if the next cell is a box, check in that direction until it's not a box
        i = 1
        while grid[y + i * dy][x + i * dx] == '[':
            i += 1
        if grid[y + i * dy][x + i * dx] == '#':
            return x, y
        else:
            grid[y + i * dy][x + i * dx] = '['
    # move the robot
    grid[y + dy][x + dx] = '@'
    grid[y][x] = '.'
    return x + dx, y + dy

def p2(filepath):
    grid, command = process_input(filepath)
    
    grid = transform_grid(grid)
    
    # find the starting position of the robot
    x, y = 0, 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                x, y = j, i
                break
    
    for c in command:
        dx, dy = dirmap[c]
        x, y = move(grid, x, y, dx, dy)
        # pretty_print(grid)
        
    print(score(grid))
    return score(grid)
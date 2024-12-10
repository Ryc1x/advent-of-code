from collections import Counter

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX


test = ''
input = ''

# read as string
with open('test') as file:
    # read as 2d array
    test = [list(line.strip()) for line in file.readlines()]

with open('input') as file:
    # read as 2d array
    input = [list(line.strip()) for line in file.readlines()]

def p1(grid):
    res = 0
    # check for 'XMAS' in the grid
    m, n  = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            # check all 8 directions, 4 char string
            for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]:
                s = ''
                for k in range(4):
                    x, y = i + k * dx, j + k * dy
                    if 0 <= x < m and 0 <= y < n:
                        # print(m,n,x, y)
                        s += grid[x][y]
                    else:
                        break
                if s == 'XMAS':
                    res += 1
    
    return res 
    
print(p1(test))
print(p1(input))

# we can allow removing one element from the array
def p2(grid):
    # check for two 'MAS' in shape of a 'X'
    # e.g.,
    # M.M
    # .M.
    # S.S
    
    res = 0
    m, n  = len(grid), len(grid[0])
    for i in range(1, m-1):
        for j in range(1, n-1):
            if grid[i][j] == 'A':
                ld = grid[i-1][j-1] + grid[i+1][j+1]
                rd = grid[i-1][j+1] + grid[i+1][j-1]
                if 'M' in ld and 'M' in rd and 'S' in ld and 'S' in rd:
                    res += 1
    
    return res

print(p2(test))
print(p2(input))
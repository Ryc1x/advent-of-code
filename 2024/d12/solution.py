import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'


# https://adventofcode.com/2024/day/12

# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE

def process_input(filename):
    # read as 2d list
    with open(filename, 'r') as file:
        return [[x for x in line.strip()] for line in file.readlines() if line.strip()]
        
    

def p1(filename):
    grid = process_input(filename)
    
    visited = set()
    m, n = len(grid), len(grid[0]) 
    regions = []
    
    for x in range(m):
        for y in range(n):
            if (x, y) in visited:
                continue
            q = [(x, y)]
            visited.add((x, y))
            perimeter = 0
            area = 0
            while q:
                i, j = q.pop()
                area += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[x][y]:
                        if (ni, nj) not in visited:
                            q.append((ni, nj))
                            visited.add((ni, nj))
                    else:
                        # boundary
                        perimeter += 1
            regions.append((area, perimeter))
        
    price = sum([area * perimeter for area, perimeter in regions])
    print(price)
    return price
    

print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)


def p2(filename):
    grid = process_input(filename)
    
    visited = set()
    m, n = len(grid), len(grid[0]) 
    # pad the grid with 0s
    grid = [[0] * (m + 2)] + [[0] + row + [0] for row in grid] + [[0] * (m + 2)]
    regions = []
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for x in range(1, m+1):
        for y in range(1, n+1):
            if (x, y) in visited:
                continue
            q = [(x, y)]
            visited.add((x, y))
            sides = 0
            area = 0
            while q:
                i, j = q.pop()
                area += 1
                for k in range(len(dirs)):
                    dx, dy = dirs[k]
                    ni, nj = i + dx, j + dy
                    pdx, pdy = dirs[(k - 1) % 4]
                    pi, pj = i + pdx, j + pdy
                    if grid[ni][nj] == grid[x][y]:
                        if grid[pi][pj] == grid[x][y]:
                            # check if that's a concave corner for A
                            # if A two adjacent neighbors of A is the same, it might be a concave corner\
                            #
                            # AA   
                            # AB   <- 'B' is the 'missing corner' (cx, cy) we want to check
                            #
                            three_corner = [(i, j), (i + dx, j + dy), (i + pdx, j + pdy)]
                            cx, cy = 0, 0
                            for px, py in three_corner:
                                cx ^= px
                                cy ^= py
                            if grid[cx][cy] != grid[x][y]:
                                sides += 1

                        if (ni, nj) not in visited:
                            q.append((ni, nj))
                            visited.add((ni, nj))
                    else:
                        # check if it's a convex corner for A 
                        #
                        # AB  <- 'A' is a convex corner of region A if two adjacent sides are different
                        # BB
                        #
                        if grid[pi][pj] != grid[x][y]:
                            sides += 1
                        
            regions.append((area, sides))
        
    # print(regions)
    price = sum([area * sides for area, sides in regions])
    print(price)
    return price

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
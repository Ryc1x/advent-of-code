import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............


def process_input(filename):
    with open(filename) as file:
        # read input as 2d array, remove trailing newline
        matrix = [list(line.strip()) for line in file if line.strip()]
        
        return matrix
        
def p1(filename):
    matrix = process_input(filename)
    m, n = len(matrix), len(matrix[0])

    posmap = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != '.':
                posmap[matrix[i][j]].append((i, j))

    # for each pair of positions, calculate the reflection point
    marks = set()
    for key, positions in posmap.items():
        for pos in positions:
            for pos2 in positions:
                if pos == pos2:
                    continue
                # calculate the reflection point
                x1, y1 = pos
                x2, y2 = pos2
                x3, y3 = 2*x2 - x1, 2*y2 - y1
                if 0 <= x3 < m and 0 <= y3 < n:
                    marks.add((x3, y3))
    
    print(len(marks))
    return len(marks)
    

print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)

def p2(filename):
    matrix = process_input(filename)
    m, n = len(matrix), len(matrix[0])

    posmap = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != '.':
                posmap[matrix[i][j]].append((i, j))

    # for each pair of positions, calculate the all the points on the line, with distance between the points
    marks = set()
    for key, positions in posmap.items():
        for pos in positions:
            for pos2 in positions:
                if pos == pos2:
                    continue
                # calculate the dx, dy
                x1, y1 = pos
                x2, y2 = pos2
                # calculate all possible points on one direction
                x, y = x2, y2
                dx, dy = x2 - x1, y2 - y1
                while 0 <= x < m and 0 <= y < n:
                    marks.add((x, y))
                    x += dx
                    y += dy
                # calculate all possible points on the other direction
                x, y = x1, y1
                dx, dy = x1 - x2, y1 - y2
                while 0 <= x < m and 0 <= y < n:
                    marks.add((x, y))
                    x += dx
                    y += dy
    print(len(marks))
    return len(marks)
    
print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
import math
import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# https://adventofcode.com/2024/day/14

# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3

def process_input(filename):
    # read as (x, y, vx, vy) list
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        return [list(map(int, re.findall(r'-?\d+', line))) for line in lines]

def pretty_print(robots, sec, m, n, fh=None):
    grid = [[' ' for _ in range(n)] for _ in range(m)]
    for x, y, _, _ in robots:
        grid[y][x] = '#'
    if fh:
        fh.write(f'Second: {sec}\n')
        for row in grid:
            fh.write(''.join(row) + '\n')
        fh.write('\n')
    else:
        print('Second:', sec)
        for row in grid:
            print(''.join(row) + '\n')
        print()
    
    # input()
    
    return grid

def calc_compactness(robots):
    # calculate the compactness of the robots
    # by calculating the distance between the robots
    # and the center of mass
    # center of mass is the average of the x and y coordinates
    # of all the robots
    cx, cy = 0, 0
    for x, y, _, _ in robots:
        cx += x
        cy += y
    cx /= len(robots)
    cy /= len(robots)
    # calculate the distance between the robots and the center of mass
    dist = 0
    for x, y, _, _ in robots:
        dist += abs(x - cx) + abs(y - cy)
    return dist

def p1(filename, width, height):
    robots = process_input(filename)
    # y - m, x - n
    m, n = height, width
    for _ in range(100):
        for i in range(len(robots)):
            x, y, vx, vy = robots[i]
            robots[i] = [(x + vx) % n, (y + vy) % m, vx, vy]
    
    # count number of points in 4 quadrants
    quadrants = [0, 0, 0, 0]
    for x, y, _, _ in robots:
        if x < n // 2 and y < m // 2:
            quadrants[0] += 1
        elif x < n // 2 and y > m // 2:
            quadrants[1] += 1
        elif x > n // 2 and y < m // 2:
            quadrants[2] += 1
        elif x > n // 2 and y > m // 2:
            quadrants[3] += 1
    
    # print(robots)
    # print(quadrants)
    res = math.prod(quadrants)
    print(res)
    return res


def p2(filename, width, height):
    robots = process_input(filename)
    # y - m, x - n
    m, n = height, width
    min_score = float('inf')
    best_robots = []
    best_sec = 0
    with open('output.txt', 'w') as file:
        for sec in range(1, 10001):
            for i in range(len(robots)):
                x, y, vx, vy = robots[i]
                robots[i] = [(x + vx) % n, (y + vy) % m, vx, vy]
            score = calc_compactness(robots)
            if score < min_score:
                min_score = score
                best_robots = [r[:] for r in robots]
                best_sec = sec
        pretty_print(best_robots, best_sec, m, n, file)

    print(best_sec)
    return best_sec

print(' -- PART 1 -- ')
p1(TEST_FILE, 11, 7)
p1(INPUT_FILE, 101, 103)

print(' -- PART 2 -- ')
p2(INPUT_FILE, 101, 103)

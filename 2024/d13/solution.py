import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# https://adventofcode.com/2024/day/13

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279

def process_input(filename):
    # read as 2d list
    with open(filename, 'r') as file:
        # machines, split by \n\n
        blocks = [line.strip() for line in file.read().split('\n\n') if line.strip()]
        # extract numbers from each block
        machines = [tuple(map(int, re.findall(r'\d+', block))) for block in blocks]
        return machines
    
    
# cost of button A is 3
# cost of button B is 1
# find the minimum cost to reach the prize

def cost(m):
    ax, ay, bx, by, tx, ty = m
    maxa = min(tx // ax, ty // ay)
    best = float('inf')
    for a in range(maxa + 1):
        rx, ry = tx - a * ax, ty - a * ay
        if rx > 0 and ry > 0 and rx % bx == 0 and ry % by == 0 and (rx // bx) == (ry // by):
            b = rx // bx
            if a * 3 + b < best:
                best = a * 3 + b
    return best if best != float('inf') else -1

def p1(filename):
    machines = process_input(filename)
    # print(machines)
    res = []
    for m in machines:
        c = cost(m)
        if c >= 0:
            res.append(c)
    print(sum(res))
    return sum(res)
        

print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)


# Time to refresh my rusty linear algebra :D
def cost_liner_alg(a1, a2, b1, b2, c1, c2):
    # solve a 2x2 linear system
    # x is the number of button A
    # y is the number of button B
    # a1 * x + b1 * y = c1
    # a2 * x + b2 * y = c2
    
    det = a1 * b2 - a2 * b1
    if det == 0:
        return -1
    
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    
    # check if x and y are non-negative, integer solution
    if x < 0 or y < 0 or x % 1 != 0 or y % 1 != 0:
        return -1
    
    return int(x * 3 + y)


def p2(filename):
    machines = process_input(filename)
    res = []
    for m in machines:
        ax, ay, bx, by, tx, ty = m
        tx, ty = tx + 10000000000000, ty + 10000000000000
        c = cost_liner_alg(ax, ay, bx, by, tx, ty)
        if c >= 0:
            res.append(c)
    print(sum(res))
    return sum(res)

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
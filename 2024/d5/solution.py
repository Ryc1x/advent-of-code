import collections, itertools, functools, re

# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47

# with open('input') as file:
#     # read as 2d array
#     input = file.read().split('\n\n')
#     ordering = [list(map(int, line.split('|'))) for line in input[0].split('\n')]
#     lists = [list(map(int, line.split(','))) for line in input[1].split('\n')]

TEST_FILE = 'test'
INPUT_FILE = 'input'

def process_input(filename):
    with open(filename) as file:
        # read the first section as list of pairs, and the second section as list of integers
        # first section is the list of pairs, second section is the list of integers
        test = file.read().split('\n\n')
        ordering = [list(map(int, line.split('|'))) for line in test[0].split('\n')]
        lists = [list(map(int, line.split(','))) for line in test[1].split('\n')]
        
    return ordering, lists

def p1(filename):
    ordering, lists = process_input(filename)
        
    # build a directed graph from the ordering
    graph = collections.defaultdict(set)
    for a, b in ordering:
        graph[a].add(b)
    
    def valid(arr):
        # returns True if the line is valid, False otherwise
        prevs = []
        for n in arr:
            for prev in prevs:
                if prev in graph[n]:
                    # print(n, prev)
                    return False
            prevs.append(n)
        return True
        
    res = 0
    for l in lists:
        if valid(l):
            # print(l, 'is valid', 'score:', l[len(l) // 2])
            # add mid element
            res += l[len(l) // 2]
    
    print(res)
    return res
    
print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)

# we can allow removing one element from the array
def p2(filename):
    ordering, lists = process_input(filename)
        
    # build a directed graph from the ordering
    graph = collections.defaultdict(set)
    for a, b in ordering:
        graph[a].add(b)
    
    def valid(arr):
        # returns True if the line is valid, False otherwise
        prevs = []
        for n in arr:
            for prev in prevs:
                if prev in graph[n]:
                    # print(n, prev)
                    return False
            prevs.append(n)
        return True
    
    def compare(x, y):
        if x in graph[y]:
            return -1
        if y in graph[x]:
            return 1

    res = 0
    for l in lists:
        if not valid(l):
            l.sort(key=functools.cmp_to_key(compare))
            res += l[len(l) // 2]
    
    print(res)
    return res

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
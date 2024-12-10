import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20

def process_input(filename):
    with open(filename) as file:
        # for each line, split by ':', then split the second part by ' '
        # the first part is the target, the second part is the list of integers
        lines = [line.strip().split(':') for line in file if line.strip()]
        targets = [int(line[0]) for line in lines]
        lists = [[int(num) for num in line[1].split()] for line in lines]
        
        return targets, lists
        
def calc(arr, target, prevs, idx):
    if idx == len(arr):
        # print(target, arr)
        return prevs == target
    return calc(arr, target, prevs + arr[idx], idx+1) or calc(arr, target, prevs * arr[idx], idx+1)
        
def p1(filename):
    targets, lists = process_input(filename)
    
    res = 0
    for i in range(len(targets)):
        target, arr = targets[i], lists[i]
        if calc(arr, target, arr[0], 1):
            res += target
    print(res)
    return res


print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)

def calc2(arr, target, prevs, idx):
    if idx == len(arr):
        # print(target, arr)
        return prevs == target
    return calc2(arr, target, prevs + arr[idx], idx+1) or \
           calc2(arr, target, prevs * arr[idx], idx+1) or \
           calc2(arr, target, prevs*(10**len(str(arr[idx]))) + arr[idx], idx+1)


def p2(filename):
    targets, lists = process_input(filename)
    
    res = 0
    for i in range(len(targets)):
        target, arr = targets[i], lists[i]
        if calc2(arr, target, arr[0], 1):
            res += target
    print(res)
    return res

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
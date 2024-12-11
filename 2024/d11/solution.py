import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'


# https://adventofcode.com/2024/day/11
# 125 17

def process_input(filename):
    # read as list
    with open(filename, 'r') as file:
        # read one line
        return [int(x) for x in file.readline().strip().split(' ') if x]
    

def p1(filename):
    arr = process_input(filename)
    
    for i in range(25):
        newarr = []
        for n in arr:
            if n == 0:
                newarr.append(1)
            elif len(str(n)) % 2 == 0:
                # split into two
                s = str(n)
                newarr.append(int(s[:len(s)//2]))
                newarr.append(int(s[len(s)//2:]))
            else:
                # multiply by 2024
                newarr.append(n * 2024)
        arr = newarr
        # print(' '.join(map(str, arr)))
        # input()
    
    print(len(arr))
    return len(arr)
    

print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)


def p2(filename):
    arr = process_input(filename)
    cnt = collections.Counter(arr)
    for i in range(75):
        # print(i)
        newcnt = collections.Counter()
        for k, v in cnt.items():
            if k == 0:
                newcnt[1] += v
            elif len(str(k)) % 2 == 0:
                # split into two
                s = str(k)
                newcnt[int(s[:len(s)//2])] += v
                newcnt[int(s[len(s)//2:])] += v
            else:
                # multiply by 2024
                newcnt[k * 2024] += v
        cnt = newcnt
        # print(cnt)
        # input()
    
    res = sum([v for v in cnt.values()])
    print(res)
    return res

print(' -- PART 2 -- ')
p2(TEST_FILE)
p2(INPUT_FILE)
from collections import Counter
import itertools

test = []
input = []

with open('test') as file:
    for line in file:
        test.append(list(map(int, line.split())))

with open('input') as file:
    for line in file:
        input.append(list(map(int, line.split())))

def p1(arrs):
    unsafe = 0
    for arr in arrs:
        # check if arr is strictly increasing or decreasing
        # check if arr has a difference of 3
        inc = arr[0] < arr[1]
        for a, b in itertools.pairwise(arr):
            if a == b or (a < b) != inc or abs(a - b) > 3:
                unsafe += 1 
                # print(arr, 'unsafe')
                break
        
    return len(arrs) - unsafe

print(p1(test))
print(p1(input))

# check safe
def check_safe(arr):
    inc = arr[0] < arr[1]
    for a, b in itertools.pairwise(arr):
        if a == b or (a < b) != inc or abs(a - b) > 3:
            return False
    return True

# we can allow removing one element from the array
def p2(arrs):
    safe = 0
    for arr in arrs:
        # check if arr is strictly increasing or decreasing
        # check if arr has a difference of 3
        inc = arr[0] < arr[1]
        possible_arrs = [arr]
        for i in range(len(arr)):
            possible_arrs.append(arr[:i] + arr[i+1:])
            
        if any([check_safe(a) for a in possible_arrs]):
            safe += 1
        
    return safe

print(p2(test))
print(p2(input))

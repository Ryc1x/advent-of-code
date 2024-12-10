from collections import Counter
import itertools
import re

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

test = ''
input = ''

# read as string
with open('test') as file:
    test = ''.join(file.readlines()).strip()

with open('input') as file:
    input = ''.join(file.readlines()).strip()

def p1(s):
    # read in the string, use regex match for mul(x,y) and add x*y to the sum
    # Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
    sum = 0
    for x, y in re.findall(r'mul\((\d+),(\d+)\)', s):
        sum += int(x) * int(y)
    return sum

print(p1(test))
print(p1(input))

# we can allow removing one element from the array
def p2(s: str):
    # read in the string, use regex match for mul(x,y) and add x*y to the sum
    # Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
    
    # The do() instruction enables future mul instructions.
    # The don't() instruction disables future mul instructions.

    # split the string by do() and don't()
    # for split after do(), sum the mul instructions, for split after don't(), do nothing
    # e.g, xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    # mul(2,4) and mul(8,5) are the only instructions that are executed
    
    sum = 0
    strs = s.split('do()')
    # print(strs)
    strs = [s.split('don\'t()')[0] for s in strs]
    # print(strs)
    for s in strs:
        sum += p1(s)
    
    return sum


print(p2(test))
print(p2(input))

import collections, itertools, functools, re

TEST_FILE = 'test.txt'
INPUT_FILE = 'input.txt'

# sample input
# 2333133121414131402
# convert to
# 00...111...2...333.44.5555.6666.777.888899
# then compact to
# 0099811188827773336446555566..............
# then calculate the check sum
# 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, ...
# 1928


def process_input(filename):
    with open(filename) as file:
        # read input as one list
        data = [int(d) for d in file.read().strip()]
        
        return data
        
def p1(filename):
    data = process_input(filename)
    
    disk = []
    id = 0
    for i, d in enumerate(data):
        if i % 2 == 1:
            disk.extend(['.'] * d)
            # space
        else:
            # file
            disk.extend([id] * d)
            id += 1
    
    # print(''.join([str(x) for x in disk]))
    
    # compact
    l = 0
    r = len(disk) - 1
    
    while l < r:
        # move pointer l to next empty space (.)
        while l < r and disk[l] != '.':
            l += 1
        # move pointer r to next file (digit)
        while l < r and disk[r] == '.':
            r -= 1
            
        # swap the file and space
        disk[l], disk[r] = disk[r], disk[l]
        # print(''.join([str(x) for x in disk]))
    
    res = sum([i * int(d if d != '.' else 0) for i, d in enumerate(disk)])
    # print(''.join([str(x) for x in disk]))
    print(res)
    
    return res

print(' -- PART 1 -- ')
p1(TEST_FILE)
p1(INPUT_FILE)



def p2(filename):
    data = process_input(filename)
    
    def format_disk(disk):
        cnt = collections.Counter()
        maxkey = 0
        for idx, file_id, file_len in disk:
            for i in range(file_len):
                cnt[idx + i] = file_id
                maxkey = max(maxkey, idx + i)

        disk_list = []
        for i in range(maxkey + 1):
            if i in cnt:
                disk_list.append(str(cnt[i]))
            else:
                disk_list.append('.')
        return disk_list

    # stores (idx, file_id/'sp', length)
    disk = [] 
    id = 0
    idx = 0
    for i, d in enumerate(data):
        if i % 2 == 0:
            disk.append((idx, id, d))
            idx += d
            id += 1
        else:
            disk.append((idx, '.', d))
            idx += d
    
    # from max id to 0
    fp = len(disk) - 1
    # sp = []
    # for i in range(1, 10):
    #     # find the first space that fit size i
    #     while
    # print_disk(disk)
    for id in range(id - 1, -1, -1):
        # move file pointer to the last file with id
        while fp >= 0 and disk[fp][1] != id:
            fp -= 2
        # find the first space that fit the size of the file
        sp = 1
        while sp < fp and disk[sp][2] < disk[fp][2]:
            sp += 2
        # move the file to the space
        if sp < fp:
            disk[fp] = (disk[sp][0], id, disk[fp][2])
            disk[sp] = (disk[sp][0] + disk[fp][2], '.', disk[sp][2] - disk[fp][2])
        # print_disk(disk)
    
    disk_list = format_disk(disk)
    checksum = sum([i * int(d if d != '.' else 0) for i, d in enumerate(disk_list)])
    # print(''.join(disk_list))
    print(checksum)
    return checksum
    
    
print(' -- PART 2 -- ') 
p2(TEST_FILE)
p2(INPUT_FILE)

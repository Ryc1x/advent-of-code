from collections import Counter

array1 = []
array2 = []

with open('input') as file:
    for line in file:
        a, b = line.split()
        array1.append(int(a))
        array2.append(int(b))

# read in file to two arrays
def p1():
    array1.sort()
    array2.sort()
    distance = 0
    for i in range(len(array1)):
        distance += abs(array1[i] - array2[i])
    
    # print sum of distances
    print(distance)

def p2():
    c1 = Counter(array1)
    c2 = Counter(array2)
    
    similarity = 0
    for k, v in c1.items():
        # print(k, c2[k])
        similarity += k * v * c2[k]
    
    print(similarity)
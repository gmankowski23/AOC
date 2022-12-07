import time
start = time.time()
with open('day3.txt') as f:
    data = f.read().splitlines()

#print(data)
#part 1
priorities = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}
priority = 0

for i in data:
    sac1 = i[:int(len(i)/2)]
    sac2 = i[int(len(i)/2):]
    for letter in sac1:
        if letter in sac2:
            priority += priorities[letter]
            break
print("Part 1 answer" , priority)

#part 2
#start = time.time()
groups = []
groupnum = 3
grouppriority = 0
for i in range(0, len(data), groupnum):
    groups.append(data[i:i+groupnum])
#print(groups)
for i in groups:
    sac1 = i[0]
    sac2 = i[1]
    sac3 = i[2]
    for letter in sac1:
        if letter in sac2 and letter in sac3:
            grouppriority += priorities[letter]
            break
print("Part 2 answer" , grouppriority)
print("Total time: ", time.time() - start)
    


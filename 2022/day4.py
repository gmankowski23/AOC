import time
start = time.time()
with open('day4.txt') as f:
    data = f.read().splitlines()
#print(data)

#part 1
overlaps = 0
for i in data:
    pair = i.split(",")
    p1 = pair[0].split("-")
    p2 = pair[1].split("-")
    #print(p1, p2)
    if int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]):
        overlaps+=1
    elif int(p2[0]) >= int(p1[0]) and int(p2[1]) <= int(p1[1]):
        overlaps+=1
print("Part 1 answer: ", overlaps)

#part 2
overlaps2 = 0
for i in data:
    pair = i.split(",")
    p1 = pair[0].split("-")
    p2 = pair[1].split("-")
    #print(p1, p2)
    if int(p1[0]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]):
        overlaps2+=1
    elif int(p2[0]) >= int(p1[0]) and int(p2[1]) <= int(p1[1]):
        overlaps2+=1
    elif int(p1[1]) >= int(p2[0]) and int(p1[1]) <= int(p2[1]):
        overlaps2+=1
    elif int(p2[1]) >= int(p1[0]) and int(p2[1]) <= int(p1[1]):
        overlaps2+=1

print("Part 2 answer: ", overlaps2)
print("Final Time: ", time.time()-start)
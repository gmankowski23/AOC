#open day1.txt and convert to list
with open('day1.txt') as f:
    data = f.read().splitlines()
#part 1
sumlist = []
for i in data:
    if i == "":
        sumlist.append(0)
    else:
        sumlist.append(int(i))
sum = 0
addlist = []
for num in sumlist:
    sum+=num
    if num == 0:
        addlist.append(sum)
        sum = 0
print("Part 1 Answer: " , max(addlist))
#part 2
addlist.sort(reverse=True)
topthreenums = 0
for i in range(0,3):
    topthreenums += addlist[i]
print("Part 2 Answer: " , topthreenums)

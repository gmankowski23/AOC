from array import *
import time, re
start = time.time()

with open('day5.txt') as f:
    moves = f.read().splitlines()

lists = {}
lists[1] = ["F","D","B","Z","T","J","R","N"]
lists[2] = ["R","S","N","J","H"]
lists[3] = ["C","R","N","J","G","Z","F","Q"]
lists[4] = ["F","V","N","G","T","T","Q"]
lists[5] = ["L","T","Q","F"]
lists[6] = ["Q","C","W","Z","B","R","G","N"]
lists[7] = ["F","C","L","S","N","H","M"]
lists[8] = ["D","N","Q","M","T","J"]
lists[9] = ["P","G","S"]

testLists = {}
testLists[1] = ["Z","N"]
testLists[2] = ["M","C","D"]
testLists[3] = ["P"]


# Part 1
'''
for i in moves:
    #print(i)
    numBlocks, start, end = [int(x) for x in re.findall("[0-9]+", i)]
    #print(numBlocks, start, end)
    while numBlocks > 0:
        lists[end].append(lists[start].pop())
        numBlocks -= 1
for i in lists:
    print(lists[i].pop())'''

# Part 2
for i in moves:
    #print(i)
    numBlocks, start, end = [int(x) for x in re.findall("[0-9]+", i)]
    #print(numBlocks, start, end)
    while numBlocks > 0:
        lists[end].append(lists[start].pop(len(lists[start])-numBlocks))
        #print (testLists)
        numBlocks -= 1
for i in lists:
    print(lists[i].pop())

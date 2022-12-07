#Column 1; A = Rock, B = Paper, C = Scissors
#Column 2; X = Rock, Y = Paper, Z = Scissors
#Points; 1 for Rock, 2 for Paper, and 3 for Scissors
#Points; 0 if you lost, 3 if the round was a draw, and 6 if you won

with open('day2.txt') as f:
    data = f.read().splitlines()
#print(data)
#print(data[0])
points = 0
for i in data:
    choice = i.split(" ")
    #print (choice)
    if choice[0] == "A" and choice[1] == "X":
        points += 1
        points += 3
    elif choice[0] == "A" and choice[1] == "Y":
        points += 2
        points += 6
    elif choice[0] == "A" and choice[1] == "Z":
        points += 3
        points += 0
    elif choice[0] == "B" and choice[1] == "X":
        points += 1
        points += 0
    elif choice[0] == "B" and choice[1] == "Y":
        points += 2
        points += 3
    elif choice[0] == "B" and choice[1] == "Z":
        points += 3
        points += 6
    elif choice[0] == "C" and choice[1] == "X":
        points += 1
        points += 6
    elif choice[0] == "C" and choice[1] == "Y":
        points += 2
        points += 0
    elif choice[0] == "C" and choice[1] == "Z":
        points += 3
        points += 3
print("Total Part 1 Points: " , points)

#Part 2
#X = Lose, Y = Draw, Z = Win
#Points; 1 for Rock, 2 for Paper, and 3 for Scissors
#Points; 0 if you lost, 3 if the round was a draw, and 6 if you won
newpoints = 0
for i in data:
    choice = i.split(" ")
    #print (choice)
    if choice[0] == "A" and choice[1] == "X":
        newpoints += 3
        newpoints += 0
    elif choice[0] == "A" and choice[1] == "Y":
        newpoints += 1
        newpoints += 3
    elif choice[0] == "A" and choice[1] == "Z":
        newpoints += 2
        newpoints += 6
    elif choice[0] == "B" and choice[1] == "X":
        newpoints += 1
        newpoints += 0
    elif choice[0] == "B" and choice[1] == "Y":
        newpoints += 2
        newpoints += 3
    elif choice[0] == "B" and choice[1] == "Z":
        newpoints += 3
        newpoints += 6
    elif choice[0] == "C" and choice[1] == "X":
        newpoints += 2
        newpoints += 0
    elif choice[0] == "C" and choice[1] == "Y":
        newpoints += 3
        newpoints += 3
    elif choice[0] == "C" and choice[1] == "Z":
        newpoints += 1
        newpoints += 6
print("Total Part 2 Points: " , newpoints)
import random

# Function to check if input is integer and in range
def inputCheck(Question, min, max):
    while True:
        try:
            tmp = int(input(Question))
            if tmp < min or tmp > max: int("a")
            else: return tmp
        except:
            print("Invalid input!")

# Function to show the board
def showBoard(board):
    print("=======\n Board\n=======\n")
    for i in range(len(board)):
        tmp = "  "
        for j in range(1, len(board[i])):
            if board[i][j] < 10:
                tmp += "  "
            elif board[i][j] < 100:
                tmp += " "
            tmp += str(board[i][j]) + "  "
        print(tmp + "\n")
    print("--------------------------------")

# Function to calculate how much is to be deducted
def rowScore(row):
    total = 0
    for i in range(1, len(row)):
        if row[i] == 55: total += 7
        elif row[i] % 11 == 0: total += 5
        elif row[i] % 10 == 0: total += 3
        elif row[i] % 5 == 0: total += 2
        else: total += 1
    return total

player = [[[],[],[],[]],[66,66,66,66],["You","Alice","Bob","Charlie"]]

while True:
    # Check if reset cards
    if len(player[0][0]) == 0:
        print("-- Setting cards now --")
        # Set the 104 cards in the cardpool
        cardpool = []
        for i in range(1, 105):
            cardpool.append(i)

        # Select 4 initial cards
        board = []
        for i in range(4):
            board.append([0])
            tmp = random.randint(0, len(cardpool)-1)
            board[i].append(cardpool[tmp])
            cardpool.pop(tmp)

        # Set cards for each player
        for i in range(len(player[1])):
            for j in range(10):
                tmp = random.randint(0, len(cardpool)-1)
                player[0][i].append(cardpool[tmp])
                cardpool.pop(tmp)
            player[0][i].sort()

    showBoard(board)

    # Display hand of player
    tmp = "Your cards:  "
    for i in range(len(player[0][0])):
        tmp += str(player[0][0][i]) + "  "
    print(tmp)

    # Ask player to play Card
    tmp = inputCheck("Please select a card(1-" + str(len(player[0][0])) + "):  ", 1, len(player[0][0])) - 1 
    print("--------------------------------\n")

    # Append player choice and random selection for robots to array
    submitted = []
    submitted.append([player[0][0][tmp],0])
    player[0][0].pop(tmp)
    for i in range(1,4):
        tmp = random.randint(0, len(player[0][i])-1)
        submitted.append([player[0][i][tmp], i])
        player[0][i].pop(tmp)

    submitted.sort()
    # Show cards dealt
    for i in range(len(player[0])):
        print(str(player[2][submitted[i][1]]) + ": " + str(submitted[i][0]))
    
    # Append cards to board and calculate scores
    for i in range(len(submitted)):
        tmp = []
        for j in range(4):
            if submitted[i][0] > board[j][len(board[j])-1]:
                tmp.append([board[j][len(board[j])-1], j])
        
        # Check if submitted card can be 
        if len(tmp) != 0:
            tmp.sort()
            board[tmp[len(tmp)-1][1]].append(submitted[i][0])
            # Check if row has 6 cards
            if len(board[tmp[len(tmp)-1][1]]) > 6:
                player[1][submitted[i][1]] -= rowScore(board[tmp[len(tmp)-1][1]])
                for j in range(len(board[tmp[len(tmp)-1][1]])-2):
                    board[tmp[len(tmp)-1][1]].pop(1)
        else: # If the card cannot be placed
            rows = []
            #Find row to take that costs the least score
            for j in range(4):
                rows.append([rowScore(board[j]), j])
            rows.sort()
            
            player[1][submitted[i][1]] -= rows[0][0]
            for j in range(len(board[rows[0][1]])-1):
                    board[rows[0][1]].pop(1)
            board[rows[0][1]].append(submitted[i][0])

    # Show scores
    tmp = "\nCurrent Scores:  "
    for i in range(len(player[1])):
        if player[1][i] < 10 and player[1][i] > 0:
            tmp += " "
        tmp += str(player[1][i]) + "  "
    print(tmp + "\n\n\n")

    # Check if anyone has a score lower than 1
    tmp = []
    for i in range(4):
        tmp.append([player[1][i],player[2][i]])
    tmp.sort()
    if tmp[0][0] < 1:
        break

# Announce game has ended and scores
print("----------------")
print("The game has ended!")
print("1st : " + str(tmp[3][1]) + " " + str(tmp[3][0]))
print("2nd : " + str(tmp[2][1]) + " " + str(tmp[2][0]))
print("3rd : " + str(tmp[1][1]) + " " + str(tmp[1][0]))
print("4th : " + str(tmp[0][1]) + " " + str(tmp[0][0]))
input()

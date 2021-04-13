import socket, threading, sys, random

s = socket.socket()

NAME = input('Please enter your name: ')
if NAME == "":
    NAME = "".join(random.sample("ABCDEFGHIJKMNOPQRSTUVWXYZ", 4))
print("Your name has been changed to " + NAME)

# Check if host or client
tmp = input('IP (Leave blank to host): ')
if (tmp == ''):
    # Server

    # Handle new clients
    def handler(conn, addr):
        print(f"[CONNECTION] {addr} [{user[2][len(user[2])-1]}] connected")
        conn.send('m\n\n Welcome! Please wait for the host to start the game'.encode())
        threading.Thread(target=recv, args=(conn, addr, len(user[0])-1)).start()

    # When receive message from client
    def recv(conn, addr, curr):
        global choice, subm
        while True:
            try:
                tmp = conn.recv(1024).decode()
            except:
                print(f'\nUser [{user[2][curr]}] disconnected.')
                for i in range(3):
                    user[i].pop(curr)
                break
            if (tmp[:1] == 'c'):
                choice[curr] = int(tmp[1:])
                subm += 1
    choice = []
    subm = 0
    
    def begin():
        # Broadcast message to all clients
        def send(msg, user):
            for i in range(len(user[0])-1):
                user[0][i+1].send(msg.encode())

        global user, choice, subm
        while True:
            if input() == 'start':
                if len(user[0]) > 1:
                    msg = '\nThe game is now starting\n'
                    print(msg)
                    send('m'+msg, user)
                    break
                else:
                    print('At least 2 players is required!')
        
        def rowScore(row):
            total = 0
            for i in range(1, len(row)):
                if row[i] == 55: 
                    total += 7
                elif row[i] % 11 == 0: 
                    total += 5
                elif row[i] % 10 == 0: 
                    total += 3
                elif row[i] % 5 == 0: 
                    total += 2
                else: total += 1
            return total

        choice = []
        player = [[],[],[]]
        for i in range(len(user[0])):
            player[0].append([])
            player[1].append(66)
            player[2].append(user[2][i])
            choice.append(0)
        while True:
            # Check if reset cards
            if len(player[0][0]) == 0:
                tmp = " -- Setting cards now --\n"
                print(tmp)
                for i in range(1, len(player[0])):
                    user[0][i].send(tmp.encode())
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
            
            # Show the board
            tmp = "^b =======\n  Board\n =======\n"
            for i in range(len(board)):
                tmp += '   '
                for j in range(1, len(board[i])):
                    if board[i][j] < 10:
                        tmp += "  "
                    elif board[i][j] < 100:
                        tmp += " "
                    tmp += str(board[i][j]) + "  "
                tmp += "\n\n"
            tmp += " --------------------------------\n"
            print(tmp[2:])
            subm = 0

            for i in range(1, len(player[0])):
                count = '^c'+str(len(player[0][i]))
                user[0][i].send(count.encode())
            for i in range(1, len(player[0])):
                user[0][i].send(tmp.encode())

            # Send players' hands accordingly
            for i in range(1, len(player[0])):
                
                tmp = "^h Your cards:  "
                for j in range(len(player[0][i])):
                    tmp += str(player[0][i][j]) + "  "
                user[0][i].send(tmp.encode())

            # Display hand of host player
            tmp = " Your cards:  "
            for i in range(len(player[0][0])):
                tmp += str(player[0][0][i]) + "  "
            print(tmp)


            # Ask player to play Card
            while True:
                try:
                    tmp = int(input(" Please select a card(1-" + str(len(player[0][0])) + "):  "))
                    if tmp < 1 or tmp > len(player[0][0]): 
                        int("a")
                    else: 
                        tmp -= 1
                        subm += 1
                        break
                except:
                    print(" Invalid input!")
            print(" --------------------------------\n")
            while True:
                if subm == len(player[0]):
                    break
                print('Waiting for everyone to play their cards...', end='\r')
            print()

            # Append players choices
            choice[0] = tmp
            submitted = []
            for i in range(len(player[0])):
                tmp = choice[i]
                submitted.append([player[0][i][tmp], i])
                player[0][i].pop(tmp)

            submitted.sort()
            # Show cards dealt
            tmp = ""
            for i in range(len(player[0])):
                tmp += "^m " + str(player[2][submitted[i][1]]) + ": " + str(submitted[i][0]) +"\n"
            
            for i in range(1, len(player[0])):
                user[0][i].send(tmp.encode())
            
            tmp = tmp.split('^m')
            for i in range(len(tmp)):
                print(tmp[i])
            
            
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
            tmp = "^m\n Current Scores:  "
            for i in range(len(player[1])):
                if player[1][i] < 10 and player[1][i] > 0:
                    tmp += " "
                tmp += str(player[1][i]) + "(" + player[2][i] + ")  "
            tmp += "\n\n\n"
            print(tmp[2:])
            for i in range(1, len(player[0])):
                user[0][i].send(tmp.encode())

            # Check if anyone has a score lower than 1
            tmp = []
            for i in range(len(player[0])):
                tmp.append([player[1][i],player[2][i]])
            tmp.sort(reverse=True)
            if tmp[len(tmp)-1][0] < 1:
                break

        # Announce game has ended and scores
        msg = "^end ----------------\n The game has ended!\n\n "
        for i in range(len(tmp)):
            msg += str(i+1) + ". " + str(tmp[i][1]) + " " + str(tmp[i][0]) + "\n "
        msg += ' \nPress enter to exit\n'
        print(msg[4:])
        for i in range(1, len(player[0])):
            user[0][i].send(msg.encode())
        input()
        sys.exit()


    user = [[0],[0],[]]
    user[2].append(NAME)

    # Setup server
    PORT = 9999
    s.bind(('127.0.0.1',PORT))
    s.listen(1)
    print(f'\nYou are now hosting on port [{PORT}]')
    print('Type \'start\' (without the quotations) when all players are ready\n')

    new_conn = 1
    threading.Thread(target=begin).start()
   
   # Accept incoming connections
    while (len(user[0]) < 11) and (new_conn == 1):
        conn, addr = s.accept()
        tmp = conn.recv(1024).decode()
        #if input(f"Accept connection from {addr} {tmp}?") != 'y':
        #    s.close()
        #else:
        user[0].append(conn)
        user[1].append(addr)
        user[2].append(tmp)
        threading.Thread(target=handler, args=(conn, addr)).start()

else:
    # Client

    def recv():
        while True:
            try:
                msg = s.recv(1024).decode()
            except:
                print('Connection to host lost.')
                input()
                sys.exit()

            msg = msg.split("^")
            #print(msg)

            for i in range(len(msg)):
                tmp = msg[i]
                if tmp[:1] == 'h':
                    print(tmp[1:])
                    #tmp = input(" Please select a card(1-" + str(card_num) + "):  ")
                    while True:
                        tmp = input(" Please select a card(1-" + str(card_num) + "):  ")
                        try:
                            tmp = int(tmp)
                            if tmp < 1 or tmp > card_num: 
                                int("a")
                            else: 
                                tmp -= 1
                                break
                        except:
                            print(" Invalid input!")
                    tmp = 'c' + str(tmp)
                    s.send(tmp.encode())
                    print(" --------------------------------\n")
                    print('Waiting for everyone to play their cards...\n', end='\r')
                elif tmp[:1] == 'c':
                    card_num = int(tmp[1:])
                elif tmp[:3] == 'end':
                    print(tmp[3:])
                    input()
                    sys.exit()
                else: 
                    print(tmp[1:])
            
            

    # Connect to server
    try:
        tmp = tmp.split(":")
        #s.connect((tmp,int(input('Please enter port: '))))
        s.connect((tmp[0], int(tmp[1])))
    except:
        print("ERROR: Host not found.")
        sys.exit()
    
    s.send(NAME.encode())
    threading.Thread(target=recv).start()
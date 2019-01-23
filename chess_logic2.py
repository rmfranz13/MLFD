'''don't make pieces objects (it's just too much). Just let the board position 
be described by a single array. and create a function which parses over the
array piece by piece and decides which moves are legal'''

starting_board_state = [[['b','r',0],['b','n',0],['b','b',0],['b','q',0],['b','k',0],['b','b',0],['b','n',0],['b','r',0]],
                        [['b','p',0],['b','p',0],['b','p',0],['b','p',0],['b','p',0],['b','p',0],['b','p',0],['b','p',0]],
                        [['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0]],
                        [['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0]],
                        [['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0]],
                        [['x','x',0],['x','x',0],['x','x',0],['x','x',0],['x','x',0],['w','n',0],['x','x',0],['x','x',0]],
                        [['w','p',0],['w','p',0],['w','p',0],['w','p',0],['w','p',0],['w','p',0],['w','p',0],['x','x',0]],
                        [['w','r',0],['w','n',0],['w','b',0],['w','q',0],['w','k',0],['w','b',0],['x','x',0],['w','r',0]]]

move_number = 0.0

def find_legal_moves(board_state, move_number):
    if (move_number%2.0 == 0):
        color_to_move = 'w'
        enemy_color = 'b'
    else:
        color_to_move = 'b'
        enemy_color = 'w'

    legal_moves = []

    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            #looks at one square at a time before trying to decide legal moves
            focus_square = board_state[i][j]
            if (focus_square[0] == color_to_move):
                #rook movement:
                if (focus_square[1] == 'r'):
                    #finding all possible rook moves (ignoring castling and king pins for now)
                    positive_x_distance = 7-i
                    negative_x_distance = i
                    positive_y_distance = 7-j
                    negative_y_distance = j
                    for k in range(positive_x_distance):
                        probe_square = board_state[i+k+1][j]
                        if (probe_square[0] == color_to_move):
                            break
                        elif (probe_square[0] == enemy_color):
                            legal_moves.append([[j,i],[j,i+k+1]])
                            break
                        else:
                            legal_moves.append([[j,i],[j,i+k+1]])
                    for k in range(negative_x_distance):
                        probe_square = board_state[i-k-1][j]
                        if (probe_square[0] == color_to_move):
                            break
                        elif (probe_square[0] == enemy_color):
                            legal_moves.append([[j,i],[j,i-k-1]])
                            break
                        else:
                            legal_moves.append([[j,i],[j,i-k-1]])
                    for k in range(positive_y_distance):
                        probe_square = board_state[i][j+k+1]
                        if (probe_square[0] == color_to_move):
                            break
                        elif (probe_square[0] == enemy_color):
                            legal_moves.append([[j,i],[j+k+1,i]])
                            break
                        else:
                            legal_moves.append([[j,i],[j+k+1,i]])
                    for k in range(negative_y_distance):
                        probe_square = board_state[i][j-k-1]
                        if (probe_square[0] == color_to_move):
                            break
                        elif (probe_square[0] == enemy_color):
                            legal_moves.append([[j,i],[j-k-1,i]])
                            break
                        else:
                            legal_moves.append([[j,i],[j-k-1,i]])
                elif (focus_square[1] == 'n'):
                    #finding all possible knight moves
                    try:
                        probe_square = board_state[i+1][j+2]
                        if ((probe_square[0]!=color_to_move) and ((i+1)<=7) and ((j+2)<=7)):
                            legal_moves.append([[j,i],[j+2,i+1]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i+2][j+1]
                        if ((probe_square[0]!=color_to_move) and ((i+2)<=7) and ((j+1)<=7)):
                            legal_moves.append([[j,i],[j+1,i+2]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i+2][j-1]
                        if ((probe_square[0]!=color_to_move) and ((i+2)<=7) and ((j-1)>=0)):
                            legal_moves.append([[j,i],[j-1,i+2]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i+1][j-2]
                        if ((probe_square[0]!=color_to_move) and ((i+1)<=7) and ((j-1)>=0)):
                            legal_moves.append([[j,i],[j-2,i+1]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i-1][j-2]
                        if ((probe_square[0]!=color_to_move) and ((i-1)>=0) and ((j-2)>=0)):
                            legal_moves.append([[j,i],[j-2,i-1]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i-2][j-1]
                        if ((probe_square[0]!=color_to_move) and ((i-2)>=0) and ((j-1)>=0)):
                            legal_moves.append([[j,i],[j-1,i-2]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i-2][j+1]
                        if ((probe_square[0]!=color_to_move) and ((i-2)>=0) and ((j+1)<=7)):
                            legal_moves.append([[j,i],[j+1,i-2]])
                    except IndexError:
                        print("Apparently I have to print this")
                    try:
                        probe_square = board_state[i-1][j+2]
                        if ((probe_square[0]!=color_to_move) and ((i-1)>=0) and ((j+2)<=7)):
                            legal_moves.append([[j,i],[j+2,i-1]])
                    except IndexError:
                        print("Apparently I have to print this")
    return(legal_moves)



                        

legal_moves = find_legal_moves(starting_board_state, move_number)

for i in legal_moves:
    print(i)




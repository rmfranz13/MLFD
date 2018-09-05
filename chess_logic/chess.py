"""
this file is intended to define the rules of a working chess board and
implement it such that the user can input a move and the computer will
know whether or not it is legal, also knowing when the game is done

For concise coding all relevant values are held in a single dictionary
called data_path. The class methods
"""


class ChessBoard:
    def __init__(self,board_state,board_history):
        self.board_state = board_state
        self.board_history = board_history
        return(None)

    def init_pos(self):
        self.board_state = [['wr','wn','wb','wq','wk','wb','wn','wr'],
                            ['wp','wp','wp','wp','wp','wp','wp','wp'],
                            ['','','','','','','',''],
                            ['','','','','','','',''],
                            ['','','','','','','',''],
                            ['','','','','','','',''],
                            ['bp','bp','bp','bp','bp','bp','bp','bp'],
                            ['br','bn','bb','bq','bk','bb','bn','br']]
        self.board_history = []
        return(None)

    def square_status(self,position,color):
        board_state = self.board_state
        x = position[0]
        y = position[1]
        color = color[0]
        if board_state[x][y] == '':
            status = "empty"
        elif board_state[x][y][0] == color:
            status = "friendly"
        else:
            status = "unfriendly"
        return(status)

    def whose_turn(self):
        board_history = self.board_history
        if (len(move_history)%2 == 0):
            to_move = "white"
        else:
            to_move = "black"
        return(to_move)

    def prompt_play(self):
        print("Press enter to begin")
        start_prompt = str(input("Type 'quit' to terminate: "))
        return(start_prompt)

    def update_board_state(self):
        board_state = self.board_state
        board_history = self.board_history
        move_start = list(int(input("Enter starting row,col for the piece you want to move: ")))
        move_end = list(input(int(("Enter ending row,col for the piece you want to move: "))))
        board_history.append(str(move_start)+str(move_end))
        d = {'A':1.,'B':2.,'C':3.,'D':4.,'E':5.,'F':6.,'G':7.,'H':8.}
        move_start = [d[move_start[0]]-1,move_start[1]-1]
        move_end = [d[move_end[0]]-1,move_end[1]-1]
        board_state[move_end[0]][move_end[1]] = board_state[move_start[0]][move_start[1]]
        self.board_state = board_state
        self.board_history = board_history
        return(None)

    def check(self,king_pos,all_possible_second_moves):
        

    def is_board_state_repeated(self):
        board_state = self.board_state
        board_history = self.board_history
        i = 0
        i_list = []
        while i<len(board_history):
            if (board_state == board_history[i]):
                i_list.append(i)
                i+=1
            else:
                i+=1
        return(i_list)  
        
    def move_legal(self):
        board_history = self.board_history
        return(legal)

    

class Pawn(ChessBoard):
    def __init__(self,pawn_position,pawn_color,pawn_history):
        self.pawn_position = pawn_position
        self.pawn_color = pawn_color
        self.pawn_history = pawn_history
        return(None)

    def possible_moves(self):
        pawn_position = self.pawn_position
        pawn_history = self.pawn_history
        pawn_color = self.pawn_color
        x = pawn_position[0]
        y = pawn_position[1]
        if pawn_color == "white":
            if len(pawn_history)!=0:
                moves = [[x,y+1],[x-1,y+1],[x+1,y+1]]
            else:
                moves = [[x,y+1],[x,y+2],[x-1,y+1],[x+1,y+1]]
        elif pawn_color == "black":
            if len(pawn_history)!=0:
                moves = [[x,y-1],[x-1,y-1],[x+1,y-1]]
            else:
                moves = [[x,y-1],[x,y-2],[x-1,y-1],[x+1,y-1]]
        else:
            print("Error: pawn color must either be 'white' or 'black'")
            moves = None
        return(moves)

    def legal_moves(self):
        board_state = self.board_state
        position = self.position
        history = self.history
        color = self.color
        x = position[0]
        y = position[1]
        moves = self.possible_moves()
        test_squares = [ChessBoard.square_status(i,color) for i in moves]
                
        
    

        
class ChessGame(ChessBoard):
    def __init__(self,current_state,next_state,inputs):
        self.current_state = current_state
        self.next_state = next_state
        self.inputs = inputs
        return(None)

    def terminate_program(self):
        print("Program safetly terminated")
        exit()
        return(None)

    def state0(self):
        self.prompt_play()
        return(None)

    def function_logic(self,current_state):
        return(None)

    def next_state_logic(self,current_state,inputs):
        return(next_state)

    def loop(self):
        self.current_state = 0
        while True:
            self.function_logic(self.current_state)
            self.next_state = self.next_state_logic(self.current_state,self.inputs)
            self.current_state = self.next_state










    
        
        
        

    

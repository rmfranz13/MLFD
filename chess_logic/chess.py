"""
this file is intended to define the rules of a working chess board and
implement it such that the user can input a move and the computer will
know whether or not it is legal, also knowing when the game is done

For concise coding all relevant values are held in a single dictionary
called data_path. The class methods
"""


class ChessBoard:
    def __init__(self,board_state,move_history):
        self.board_state = board_state
        self.move_history = move_history
        return(None)

    def init_pos(self):
        self.board_state = [[['wr'],['wn'],['wb'],['wq'],['wk'],['wb'],['wn'],['wr']],
                            [['wp'],['wp'],['wp'],['wp'],['wp'],['wp'],['wp'],['wp']],
                            [[''],[''],[''],[''],[''],[''],[''],['']],
                            [[''],[''],[''],[''],[''],[''],[''],['']],
                            [[''],[''],[''],[''],[''],[''],[''],['']],
                            [[''],[''],[''],[''],[''],[''],[''],['']],
                            [['bp'],['bp'],['bp'],['bp'],['bp'],['bp'],['bp'],['bp']],
                            [['br'],['bn'],['bb'],['bq'],['bk'],['bb'],['bn'],['br']]]
        self.move_history = []
        return(None)

    def prompt_play(self):
        print("Press enter to begin")
        start_prompt = str(input("Type 'quit' to terminate: "))
        return(start_prompt)

    def update_board_state(self):
        board_state = self.board_state
        move_history = self.move_history
        move_start = list(int(input("Enter starting row,col for the piece you want to move: ")))
        move_end = list(input(int(("Enter ending row,col for the piece you want to move: "))))
        move_history.append(str(move_start)+str(move_end))
        d = {'A':1.,'B':2.,'C':3.,'D':4.,'E':5.,'F':6.,'G':7.,'H':8.}
        move_start = [d[move_start[0]]-1,move_start[1]-1]
        move_end = [d[move_end[0]]-1,move_end[1]-1]
        board_state[move_end[0]][move_end[1]] = board_state[move_start[0]][move_start[1]]
        self.board_state = board_state
        self.move_history = move_history
        return(None)

    def move_legal(self)
    
    def terminate_program(self):
        print("Program safely terminated")
        exit()
        return(None)

class ChessGame(ChessBoard):
    def __init__(self,current_state,next_state,inputs):
        self.current_state = current_state
        self.next_state = next_state
        self.inputs = inputs
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










    
        
        
        

    

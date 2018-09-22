"""
this file is intended to define the rules of a working chess board and
implement it such that the user can input any move, defined by specifying
a starting square and ending square. The board then decides whether the
move is legal. In the event of an illegal move, the offending side 
immediately looses. The idea is that the AIs competing will be forced to
learn the rules though trial-and-error just like a human, as opposed to 
having the rules hard-wired into the AIs.
"""
import matplotlib.pyplot as plt


#Helper functions for building game obects

def string_to_coordinate(str_rc):
    a = str_rc[0]
    b = str_rc[1]
    if a == 'a':
        a = 1
    elif a == 'b':
        a = 2
    elif a == 'c':
        a = 3
    elif a == 'd':
        a = 4
    elif a == 'e':
        a = 5
    elif a == 'f':
        a = 6
    elif a == 'g':
        a = 7
    elif a == 'h':
        a = 8
    else:
        print("invalid column")
    x = a
    y = int(b)
    return(x,y)

#game object definitions

class Pawn:
    def __init__(self, color, position):
        self.color = color
        self.position = string_to_coordinate(position)
        return(None)

    def find_possible_moves(self):
        if self.color == 'white':
            a = 1
            b = 2
        else:
            a = -1
            b = -2

        move1 = [self.position[0],self.position[1]+a]
        move2 = [self.position[0],self.position[1]+b]
        move3 = [self.position[0]-1,self.position[1]+a]
        move4 = [self.position[0]+1,self.position[1]+a]
        dummy = [move1,move2,move3,move4]
        moves = []
        for i in dummy:
            if (i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8):
                moves.append(i)
        self.possible_moves = moves
        return(moves)

class King:
    def __init__(self, color, position):
        self.color = color
        self.position = string_to_coordinate(position) 
        return(None)

    def find_possible_moves(self):
        move1 = [self.position[0]+1,self.position[1]+1]
        move2 = [self.position[0]+1,self.position[1]]
        move3 = [self.position[0]+1,self.position[1]-1]
        move4 = [self.position[0],self.position[1]-1]
        move5 = [self.position[0]-1,self.position[1]-1]
        move6 = [self.position[0]-1,self.position[1]]
        move7 = [self.position[0]-1,self.position[1]+1]
        move8 = [self.position[0],self.position[1]+1]
        dummy = [move1,move2,move3,move4,move5,move6,move7,move8]
        moves = []
        for i in dummy:
            if (i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8):
                moves.append(i)
        self.possible_moves = moves
        return(moves)

class Rook:
    def __init__(self, color, position):
        self.color = color
        self.position = string_to_coordinate(position)
        return(None) 

    def find_possible_moves(self):
        dummy = []
        for i in range(7):
            dummy.append([self.position[0]+i+1,self.position[1]])
            dummy.append([self.position[0]-i-1,self.position[1]])
            dummy.append([self.position[0],self.position[1]+i+1])
            dummy.append([self.position[0],self.position[1]-i-1])
        moves = []
        for i in dummy:
            if (i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8):
                moves.append(i)
        self.possible_moves = moves
        return(moves)

class Bishop:
    def __init__(self, color, position):
        self.color = color
        self.position = string_to_coordinate(position)
        return(None)

    def find_possible_moves(self):
        dummy = []
        for i in range(7):
            dummy.append([self.position[0]+i+1,self.position[1]+i+1])
            dummy.append([self.position[0]+i+1,self.position[1]-i-1])
            dummy.append([self.position[0]-i-1,self.position[1]-i-1])
            dummy.append([self.position[0]-i-1,self.position[1]+i+1])

        moves = []
        for i in dummy:
            if (i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8):
                moves.append(i)
        self.possible_moves = moves
        return(moves)

class Queen:
    def __init__(self, color, position):
        self.color = color
        self.position = string_to_coordinate(position)
        return(None)

    def find_possible_moves(self):
        dummy = [] 
        for i in range(7):
            dummy.append([self.position[0]+i+1,self.position[1]])
            dummy.append([self.position[0]-i-1,self.position[1]])
            dummy.append([self.position[0],self.position[1]+i+1])
            dummy.append([self.position[0],self.position[1]-i-1])
            dummy.append([self.position[0]+i+1,self.position[1]+i+1])
            dummy.append([self.position[0]+i+1,self.position[1]-i-1])
            dummy.append([self.position[0]-i-1,self.position[1]-i-1])
            dummy.append([self.position[0]-i-1,self.position[1]+i+1])
        moves = []
        for i in dummy:
            if (i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8):
                moves.append(i)
        self.possible_moves = moves
        return(None)

class Knight:
    def __init__(self, color, position):
        self.color = color
        self.position = string_to_coordinate(position)
        return(None)

    def find_possible_moves(self):
        move1 = [self.position[0]+1,self.position[1]+2]
        move2 = [self.position[0]+2,self.position[1]+1]
        move3 = [self.position[0]+2,self.position[1]-1]
        move4 = [self.position[0]+1,self.position[1]-2]
        move5 = [self.position[0]-1,self.position[1]-2]
        move6 = [self.position[0]-2,self.position[1]-1]
        move7 = [self.position[0]-2,self.position[1]+1]
        move8 = [self.position[0]-1,self.position[1]+2]
        dummy = [move1,move2,move3,move4,move5,move6,move7,move8]
        moves = []
        for i in dummy:
            if (i[0]>=1 and i[0]<=8 and i[1]>=1 and i[1]<=8):
                moves.append(i)
        self.possible_moves = moves
        return(moves)


# Helper functions for game logic

def coordinate_to_string(x,y):
    letters = ['a','b','c','d','e','f','g','h']
    a = letters[x]
    b = str(y)
    str_rc = a+b
    return(str_rc)

position = 'g5'
king1 = King('white',position)
possible_moves = king1.find_possible_moves()
x_list = []
y_list = []
for i in possible_moves:
    x_list.append(i[0])
    y_list.append(i[1])
x_list.append(string_to_coordinate(position)[0])
y_list.append(string_to_coordinate(position)[0])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x_list,y_list)
plt.show()





    
        
        
        

    

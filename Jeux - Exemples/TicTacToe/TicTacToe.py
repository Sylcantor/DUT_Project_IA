class Board(object):
    #init to initialise list of cells with length 9
    def __init__(self):
        self.cells = [" "]*9

    #displays board in a presentable order
    def display(self):
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('------')
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('------')
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])

    #updates board
    def update(self, cell_num, player):
        if self.cells[cell_num-1] == " ":
            self.cells[cell_num-1] = player
            
    #checks all conditions for winner
    def iswinner(self, player):

        #horizontal cells check
        if (self.cells[0]==player and self.cells[1]==player and self.cells[2]==player):
            return True
        if (self.cells[3]==player and self.cells[4]==player and self.cells[5]==player):
            return True
        if (self.cells[6]==player and self.cells[7]==player and self.cells[8]==player):
            return True
        
        #vertical cells check
        if (self.cells[0]==player and self.cells[3]==player and self.cells[6]==player):
            return True
        if (self.cells[1]==player and self.cells[4]==player and self.cells[7]==player):
            return True
        if (self.cells[2]==player and self.cells[5]==player and self.cells[8]==player):
            return True
        
        #diagonal cells check
        if (self.cells[0]==player and self.cells[4]==player and self.cells[8]==player):
            return True
        if (self.cells[2]==player and self.cells[4]==player and self.cells[6]==player):
            return True

    #resets board to null
    def reset(self):
        self.cells = [" "]*9

    #checks for tie
    def check(self):
        used = 0
        for cell in self.cells:
            if cell != " ":
                used = used + 1
        if used == 9:
            return True
        else:
            return False
        
#object board from class Board
board = Board()

def Welcome():
    print("Welcome to tic tac toe\n")
    board.display()

Welcome()

while True:
    
    #get X input
    x = int(input("\n Please choose from 1-9\n (X)\n "))
    board.update(x, "X")
    board.display()

    #check if X is winner
    if(board.iswinner("X")):
        print('\n X wins !')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break

    #check if it is a tie
    if(board.check()):
        print('\n Tie!')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break
        
    #get o input
    o = int(input("\n Please choose from 1-9\n (o)\n "))
    board.update(o, "o")
    board.display()

    #check if o is winner
    if(board.iswinner("o")):
        print('\n o wins !')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break
        
    #check if it is a tie
    if(board.check()):
        print('\n Tie !')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break

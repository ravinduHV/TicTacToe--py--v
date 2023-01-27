"""
Program by Vimarshana Herath.
CS50p final project.
Kurunegala, Sri Lanka.
'Tic Tac Toe'
 ___ ___ ___
|___|___|_x_|
|___|_o_|___|
|_x_|___|___|

"""

import random
import dinosay 


secret_moves=[
        [(1,1), (3,3)],
        [(1,3), (3,1)],
        [(1,2), (3,2)],
        [(2,1), (2,3)]
    ]

def Board(figures=[]):
    board = ""
    filled_cells=[figure[0] for figure in figures]
    sign = [figure[1] for figure in figures]
    board += ' ._1_._2_._3_.\n'
    for row in range(4)[1:]:
        board += f'{row}|'
        for cell in range(4)[1:]:
            if (cell, row) in filled_cells:
                c = filled_cells.index((cell,row))
                board += f'_{sign[c]}_|'
            else:
                board += '___|'
        board += "\n"
    return board
        
def deside_figure():
    while True:
        opponent = input('Sign (X/O):').strip().upper()
        if opponent == 'X':
            mySign = 'O'
            break
        elif opponent == 'O':
            mySign = 'X'
            break
        else:
            print('Usage  type "X" or "x" or "O" or "o"')
    return mySign, opponent

def opponetMove(filled_cells):
    while True:
            try:
                moveX, moveY = map(int , input("Move :").strip().split(','))
                if not 3 >= moveX > 0 or not 3 >= moveY > 0:
                    raise ValueError
                if (moveX,moveY) in filled_cells:
                    raise TypeError
                break
            except:
                print("Usage  [Move :X(:int),Y(:int)]")
    return moveX, moveY
        
def cells_arround(x,y, all_cells):
    new_permutations = [(i,j) for i in range(x+2)[(x-1):] for j in range(y+2)[(y-1):]]
    return [cell for cell in new_permutations if cell in all_cells and cell !=(x,y) ]

def axis():
    return [
        [(1,1), (2,2), (3,3)],
        [(3,1), (2,2), (1,3)],
        [(1,1), (2,1), (3,1)],
        [(1,2), (2,2), (3,2)],
        [(1,3), (2,3), (3,3)],
        [(1,1), (1,2), (1,3)],
        [(2,1), (2,2), (2,3)],
        [(3,1), (3,2), (3,3)]
        
    ]
    
def Iwins(moves, side, axis_lines):
    cells = [move[0] for move in moves if move[1] == side]
    
    for line in axis_lines:
        counter = 0
        for cell in cells:
            if cell in line:
                counter += 1
        if counter == 3:
            return True
    return False    

def try_to_win(moves, mySide, opponent, empty_cells, axis_lines=axis()):
    my_cells = [move[0] for move in moves if move[1] == mySide]
    oppo_cells = [move[0] for move in moves if move[1] == opponent]
    for line in axis_lines:
        counter = 0
        for myCell in my_cells:
            if myCell in line:
                counter += 1
                for Ocells in oppo_cells:
                    if Ocells in line:
                        counter = 0
                        break
        if counter == 2:
            next_move = [cell for cell in line if cell in empty_cells]
            return next_move        
    return None

def main():
    mySide, oppositionSide = deside_figure()
    permutations = [(i,j) for i in range(4)[1:] for j in range(4)[1:]]
    filled_cells = []
    moves =[]
    axis_arrays = axis()
    
    while True:
        if oppositionSide == 'O' and not moves:
            my_move = random.choice(permutations)
            filled_cells.append(my_move)
            moves.append([my_move, mySide])
        print(Board(moves))
        
        if Iwins(moves, mySide, axis()):
            msg = "You Lose!!! Try again"
            dinosay.dinoprint(msg, dinosay.DINO_TYPE['parasaurolophus'], 'red')
            break
        OmoveX, OmoveY = opponetMove(filled_cells)
        filled_cells.append((OmoveX, OmoveY))
        moves.append([(OmoveX, OmoveY), oppositionSide])
        empty_cells = [cell for cell in permutations if cell not in filled_cells]
        
        cells_around = cells_arround(OmoveX, OmoveY, permutations)
        wins = False
        maked_move = False
        
        winning_move = try_to_win(moves, mySide, oppositionSide, empty_cells)
        
        
        for cell in cells_around:
            if cell in filled_cells:
                if [move for move in moves if move[0] == cell and move[1] == oppositionSide]:
                    for line in axis_arrays:
                        if cell in line and (OmoveX, OmoveY) in line:
                            move_cell = [x for x in line if x != cell and x != (OmoveX, OmoveY)][0]
                            if moved:= [move for move in moves if move[0] == move_cell]:
                                if moved[0][1] == oppositionSide:
                                    print(Board(moves))
                                    msg = "Congragulations! , You Win!!"
                                    dinosay.dinoprint(msg, dinosay.DINO_TYPE['tyrannosaurus'],'blue')
                                    wins = True
                                    maked_move = True
                                    return 0
        for cell in cells_around:
            if cell in filled_cells:
                if [move for move in moves if move[0] == cell and move[1] == oppositionSide]:
                    for line in axis_arrays:
                        if cell in line and (OmoveX, OmoveY) in line:
                            move_cell = [x for x in line if x != cell and x != (OmoveX, OmoveY)][0]
                            if not winning_move and move_cell in empty_cells:  
                                filled_cells.append(move_cell)
                                moves.append([move_cell, mySide])
                                maked_move = True
                                break
            if maked_move:
                break
        for cell in cells_around:
            if cell in empty_cells and not maked_move and not winning_move:
                    for line in axis_arrays:
                        if cell in line and (OmoveX, OmoveY) in line:
                            move_cell = [cell_ for cell_ in line if cell_ != cell and cell_ != (OmoveX, OmoveY)][0]
                            if [move for move in moves if move[0] == move_cell and move[1] == oppositionSide]:
                                filled_cells.append(cell)
                                moves.append([cell, mySide])
                                maked_move = True
            elif winning_move:
                filled_cells.append(winning_move[0])
                moves.append([winning_move[0], mySide])
                maked_move = True
                
            if maked_move:
                break
        if not maked_move and len(filled_cells) == 1:
            for secret in secret_moves:
                if (OmoveX,OmoveY) in secret:
                    my_first_move = [cell for cell in secret if cell != (OmoveX, OmoveY)][0] 
                    filled_cells.append(my_first_move)
                    moves.append([my_first_move, mySide])
                    maked_move = True
        if not maked_move and len(empty_cells) != 0:
            my_move = random.choice(empty_cells)
            filled_cells.append(my_move)
            moves.append([my_move, mySide])
            maked_move = True
        
        if not [cell for cell in permutations if cell not in filled_cells] and not wins and not Iwins(moves, mySide, axis()):
            print(Board(moves))
            msg = "Draw"
            dinosay.dinoprint(msg, dinosay.DINO_TYPE['ankylosaur'], 'green')
            return 0    
        
        if wins:
            return 0
    
if __name__=="__main__":
    main()



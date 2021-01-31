import random
from math import exp
import time
from copy import deepcopy
import numpy as np 

N_QUEENS = 8
TEMPERATURE = 4000


def create_board(n):

    row = []
    col = [] 
    temp1 = list(range(n))
    temp2 =  list(range(n))
    random.shuffle(temp1)
    random.shuffle(temp2)  
    
    chess_board = []
    x=0
    
    while x < n:
        rand_row = random.choice(temp1)
        rand_col = random.choice(temp2)

        if [rand_row, rand_col] not in chess_board:
            chess_board.append([rand_row, rand_col]) 
            x += 1 
                         
    return chess_board

def cost(chess_board):
    
    threat = 0
    for x in range(N_QUEENS):
        for y in range(x+1, N_QUEENS):
            
            if chess_board[x][0] == chess_board[y][0]:
                threat += 1
    
            if chess_board[x][1] == chess_board[y][1]:
                threat += 1
                
            if abs(chess_board[y][0] - chess_board[x][0]) == abs(chess_board[y][1] - chess_board[x][1]):
                threat += 1
                
    return threat 


def move(board):
    
    while True:
        choice = random.choice(board)
        row_random = random.choice(range(N_QUEENS))
        col_random = random.choice(range(N_QUEENS))

        if [row_random,col_random] in board:
            continue
        
        if choice[0] != row_random and \
        choice[1] != col_random and \
        abs(row_random - choice[0]) != abs(col_random - choice[1]):
            continue
        
        for elm in board:
            if elm != choice and \
            elm[0] in range(choice[0], row_random) and \
            elm[1] in range(choice[1], col_random):
                if (elm[1] - col_random) == ((col_random - choice[1])/(row_random - choice[0]))*(elm[0]-row_random):
                    continue                      
                
        board.remove(choice)
        board.append([row_random,col_random])
        break
    return board    


def print_chess_board(board):
    
    elements = np.array([[' ']*N_QUEENS]*N_QUEENS)
     
    for elm in board:
        elements[elm[0],elm[1]] = "*"
            
    print(elements)
    print('\n'+str(cost(board))+'\n')
    print('\n'+'----------------------'+'\n')
    
    

def simulated_annealing():
    
    board = create_board(N_QUEENS)
    solution_found = False
    
    print_chess_board(board)
    
    t = TEMPERATURE
    sch = 0.99
    cost_board = cost(board)
    
    while t > 0:
        t *= sch
        successor = deepcopy(board)
        move(successor)
        delta = cost(successor) - cost_board
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            board = deepcopy(successor)
            print_chess_board(board)
            cost_board = cost(board)
        if cost_board == 0:
            solution_found = True
            print_chess_board(board)
            break
    if solution_found is False:
        print("Failed")
        
        
start = time.time()
simulated_annealing()
print("Runtime in second:", time.time() - start)


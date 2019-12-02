# rule personalization
SLOPE_OF_POS_DIAG = (1,1)  # define slope of diagonal
SLOPE_OF_NEG_DIAG = (-1,1)
SLOPE_OF_POS_TENG = (-1,-1)
SLOPE_OF_NEG_TENG = (1,-1)  
SLOPE_OF_POS_HORI = (1,0)
SLOPE_OF_NEG_HORI = (-1,0)
SLOPE_OF_POS_VERT = (0,-1)
SLOPE_OF_NEG_VERT = (0,-1)
# table personalization
ROW = 8                         # num of row for chess board
COLUMN = 8                      # num of col for chess board
COL_LEFT = '+'
COL_MID = '---'
COL_RIGH = '+'
ROW_LEFT = '| '
ROW_NORM = ' | '
ROW_RIGH = ' |'
EMPTY = ' '
# chess personalization
PLAYER_SOLAR = 'o'
PLAYER_LUNAR = 'x'
MODE_ONE = "Human vs AI"
MODE_TWO = "Human vs Human"

table = []
slope = [[0]*8,[SLOPE_OF_POS_DIAG, SLOPE_OF_NEG_DIAG, SLOPE_OF_POS_TENG, SLOPE_OF_NEG_TENG, SLOPE_OF_POS_HORI, SLOPE_OF_NEG_HORI, SLOPE_OF_POS_VERT, SLOPE_OF_NEG_VERT]]

'''
get_init_table(x,y) returns empty table with x row and y colnum
get_init_table()    returns fresh(empty) table with default row*col
'''
def get_init_table(row = ROW, col = COLUMN):
    return [[EMPTY]*row for i in range(col)]
    #return [[EMPTY]* row] * col


def print_table():
    col_print = EMPTY
    for i in range(COLUMN):
        col_print = col_print + EMPTY * 2 + str(i) + EMPTY
    col_print = col_print + EMPTY*2 + "X"
    print(col_print)
    col_print = EMPTY + (COL_LEFT + COL_MID) * ROW + COL_RIGH
    print(col_print)
    i = 0
    for row in table:
        row_print = str(i) + ROW_LEFT + ROW_NORM.join(row) + ROW_RIGH
        i = i +1
        print(row_print)
        print(col_print)
    print("Y")
        #col_index = 0
        #row_print = ''
        #while col_index < COLUMN:
            #if col_index == 0:              # printing most left element
                #row_print = ROW_LEFT + row[col_index]
            #elif col_index == COLUMN-1:     # printing most righ element
                #row_print = ROW_NORM + row[col_index] + ROW_RIGH
            #else:                           # printing middle element
                #row_print = ROW_NORM + row[col_index]
            #print(row_print)
            #col_index += 1

#'''
#The code needs to change when we want to check interlaced(cross the row)
#since it involves a different list
#(left_slop,right_slop) = (-1,1) check diagonal \
#(left_slop,right_slop) = (1,-1) check diagonal /
#(left_slop,right_slop) = (0,0) check  col      |
#'''


def check_valid(x, y):
    '''
    check_valid(x, y) returns if the coord you choose is valid
    >>>Example: check_valid(0,0)
                True
		check_valid(3,3)
		False
    '''     
    if y < 0 or y >= COLUMN or x < 0 or x >= COLUMN:
	#Chess cannot be placed outside the board
        Result = False
    elif table[y][x] != EMPTY:
	#Chess cannot be placed on a coord where there is already a chess
        Result = False
    else:
	#if a coord is in the board and is empty, it is valid
        Result = True
    return Result

def check_one_slope(x, y, COLOUR, index):
    '''
    check_one_slope(x, y, COLOUR, index) returns the number of chesses need to be flipped on one line
    >>>Example: check_one_slop(2,3,PLAYER_LUNAR, 4)
                1
    ''' 
    (slope_X, slope_Y) = slope[1][index]
    index_X = x + slope_X
    index_Y = y + slope_Y
    number = 0 #a temp storage of "time"
    time = 0 #time is to show how many chesses do we need to flip
    while index_X < ROW and index_X >= 0 and index_Y < COLUMN and index_Y >= 0:
        #Stop when we exceed the board
        if table[index_Y][index_X] == COLOUR and (index_X != x + slope_X or index_Y != y + slope_Y):
            time = number
            break
        elif table[index_Y][index_X] == EMPTY:
	    #Stop when we find an EMPTY
            number = 0
            break
        elif table[index_Y][index_X] != COLOUR:
            #If the next chess is the opponent colour then keep checking
            index_X += slope_X
            index_Y += slope_Y
            number += 1
        else:
            #Stop when we find a chess of the same colour just next to the original chess
            number = 0
            break 
    return time

def flip_chess(x, y, COLOUR):
    '''
    flip_chess(x, y, COLOUR) change the colour of the chesses
    must run after check()
    >>>Example: flip_chess(2,3,PLAYER_LUNAR)
   0   1   2   3   4   5   6   7   X
 +---+---+---+---+---+---+---+---+
0|   |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+---+
1|   |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+---+
2|   |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+---+
3|   |   | x | x | x |   |   |   |
 +---+---+---+---+---+---+---+---+
4|   |   |   | x | o |   |   |   |
 +---+---+---+---+---+---+---+---+
5|   |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+---+
6|   |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+---+
7|   |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+---+
Y
    '''         
    table[y][x] = COLOUR
    for i in range (8): 
        #set the slope by the list
        (slope_X, slope_Y) = slope[1][i]
	#count how many chess do we need to flip
        time = slope[0][i]
        #Now we can flip the chess
        for i in range(time):
            x += slope_X
            y += slope_Y
	    #change the colour
            table[y][x] = COLOUR
    #Show the table after this turn ends
    print_table()
    return None

def check(x, y, COLOUR):
    '''
    check(x, y, COLOUR) returns whether a coord is availavle and valid.
    >>>Example: check(2,3,PLAYER_LUNAR)
	        True
    ''' 
    sum = 0
    if check_valid(x,y):
        for i in range(8):
	    #Sets the number of pieces to flip in each direction
            slope[0][i] = check_one_slope(x, y, COLOUR, i)
	    #Count the number of pieces that can be flipped 
            sum += slope[0][i]
        if sum != 0:
	    #This coord is invalid if it is already occupied and no pieces can be flipped
            Result = True
        else:
            Result = False
    else:
        Result = False
    return (Result, sum)

def check_board():
    Result = False
    sum = 0
    for row in table:
        for i in range(COLUMN):
            if row[i] == EMPTY:
                sum += 1
    if sum != 0:
        Result = True
    return Result

def check_available_step(COLOUR, status):
    '''
    check_available_step(COLOUR) returns whether there is valid coord on the board that can flip at least one piece and show the available steps in this turn.
    >>>Example: check_available_step(PLAYER_LUNAR)
	        True
    '''     
    available_step = "Available step for player " + COLOUR + ": "
    #num is the Y-coord
    num = 0
    result = 0
    sum = 0
    x = 0
    y = 0
    for row in table:
	#i is the X-coord
        for i in range(COLUMN):
	    #For each line in the list, check every item
            (Result, temp) = check(i, num, COLOUR)
            if Result:
		#If an item is valid, record the coord and add it to the available_step
                available_step = available_step + str(i) + "," + str(num) + "; "
		#record the amount of available steps
                if temp > sum:
                    sum = temp
                    x = i
                    y = num
        num += 1
    if sum == 0:
	#return false if there is no available step
        if status == 1:
            print("No available step for player " + COLOUR)
        result = False
    else:
	#show the available coord and return True if there is at least one available step
        if status == 1:
            print(available_step)
        result = True
    return (result, x, y)

def enter_a_coord():
    '''
    enter_a_coord() asks player to input a coord to display their chess and check if the coord is in the format(three characters, the first and the third are integers from 0 to 7 and the second one are ",")
    '''    
    Result = False
    while not(Result):
        coord = input("Please enter a coordinate, ex:1,2 :")
        if len(coord) == 3:
            X = coord[0]
            Y = coord[2]
            space = coord[1]
            valid_num = ["0","1","2","3","4","5","6","7"]
            if X in valid_num and Y in valid_num and space == ",":
                Result = True
            else:
                Result = False
        else:
            Result = False
        if not(Result):
            print("please enter a coordinate like the example: x,y (x,y are integers from 0 to 7)")
    return (int(X),int(Y))

def display_chess(COLOUR):
    '''
    display_chess(COLOUR) enables one player to run his turn (place one chess and flip the opponent's chess)
    '''       
    #Show which player you are in this turn
    print("You are player " + COLOUR)
    #Keep asking player to enter a coord until player enters a valid coord(the result is true)
    #Set the result false at first
    result = False
    while not(result):
        print("You must enter a valid coordinate to flip the opponent's chess")
	#Make the input answer two integers
        coord = enter_a_coord()
	#Assign values to the X-coord and Y-coord
        (X,Y) = coord
        (result,sum) = check(X,Y,COLOUR)
    #Now we can flip the chess
    flip_chess(X, Y, COLOUR)

    return None

def count(COLOUR):
    '''
    count(COLOUR) counts the total number of a specific item on the board
    '''
    #Start from 0
    sum = 0
    #Check each line in the list
    for row in table:
	#Count the number of selected item in each line and add it to the sum
        sum += row.count(COLOUR)
    #Show the number of the item
    print("numbers of " + COLOUR + ": " + str(sum))
    #The 
    return sum

def show_result():
    '''
    show_result() showes the winner of the game by comparing the amount between balck chesses and white chesses
    '''
    #Count the amount of black chesses
    sum_black = int(count(PLAYER_LUNAR))
    #Count the amount of white chesses
    sum_white = int(count(PLAYER_SOLAR))
    #Count the amount of empty blocks
    sum_empty = int(count(EMPTY))
    #Compare the numbers, the player with more chesses wins.
    if sum_black > sum_white:
        print("Player " + PLAYER_LUNAR + " wins.")
        print("Congratulations!")
    elif sum_black < sum_white:
        print("player " + PLAYER_SOLAR + " wins.")
        print("Congratulations!")
    else:
        print("Games drawn.")
    return None

def change_player(COLOUR):
    '''
    change_player(COLOUR) change the current colour at the end of each round to start the next.
    >>>Exampler: change_player(PLAYER_LUNAR)
                 o
    '''
    #Change the current colour to the opponent's colour
    if COLOUR == PLAYER_LUNAR:
        COLOUR = PLAYER_SOLAR
    else:
        COLOUR = PLAYER_LUNAR
    return COLOUR

def play(mode):
    print_table()
    colour = PLAYER_LUNAR
    (Result_X,x,y) = check_available_step(PLAYER_LUNAR,0)
    (Result_O,x,y) = check_available_step(PLAYER_SOLAR,0)
    while Result_O or Result_X:
        (Result, x, y) = check_available_step(colour,0)
        if not(Result):
            colour = change_player(colour)
        if mode == MODE_ONE and colour == PLAYER_SOLAR:
            (Result, x, y) = check_available_step(colour,0)
            print("AI placed a chess on (" + str(x) + "," + str(y) + ").")
            check(x, y, colour)
            flip_chess(x, y, colour)
        else:
            check_available_step(colour,1)
            display_chess(colour)
        colour = change_player(colour)
        if not(check_board()):
            break
    print("No available step on the board.")
    show_result()

def reset_table():
    '''
    reset_table() clean the table and set it to the original status when a new game starts.
    '''
    #Clear the items in the table line by line, one by one
    for row in table:
        for i in range(COLUMN): 
            if row[i] != EMPTY:
                row[i] = EMPTY
    #Set the first four pieces in the center of the chessboard
    #Pieces of the same colour are on a diagonal line.
    table[3][3] = PLAYER_SOLAR
    table[4][4] = PLAYER_SOLAR
    table[3][4] = PLAYER_LUNAR
    table[4][3] = PLAYER_LUNAR
    return None

def select_mode(MODE):
    '''
    select_mode(MODE) changes the mode between "Human vs. AI" and "Human vs. Human".
    >>>Example: select_mode(MODE_ONE)
                Human vs. Human
    '''
    #MODE_ONE means one player, MODE_TWO means two players
    #Change the current mode to another mode
    if MODE == MODE_ONE:
        MODE = MODE_TWO
    else:
        MODE = MODE_ONE
    #Notice the player that mode has been changed
    print("Mode has been changed successfully!")
    return MODE

def main():
    start_the_game = True
    mode = MODE_TWO
    while start_the_game:
        print("Current mode: " + mode)
        answer = input("Press START to start. Press MODE to change mode :")
        if answer == "START":
            play(mode)
            answer = input("Wanna play again? Press YES to start another game. Press anything else to quit:")
            if answer == "YES":
                reset_table()
                play(mode)
            else:
                start_the_game = False
                print("Game over.")
        elif answer == "MODE":
            mode = select_mode(mode)
        else:
            print("please enter a valid key word")
    print("Thanks for playing this game :)")
    return None

table = get_init_table()
reset_table()
main()
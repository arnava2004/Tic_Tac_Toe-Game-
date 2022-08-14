#Blank Slate for Game
from inspect import Traceback
import itertools
 
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

#Iteration
def win(current_game):
    
    def all_same(L):
        if L.count(L[0]) == len(L) and L[0]!=0:
            return True
        else:
            return False
    all_match=True
    #Checks Horizontal winner
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True
    #Checks Vertical Winner
    for col in range(len(game[0])):
        check=[]
    #Checking if each item in column 0 matches, vertical winner thingz
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True
    #Checks diagonal winner!
    diag =[]
    for idx,reverse_idx in enumerate(reversed(range(len(game)))):
        diag.append(game[idx][reverse_idx])

    if all_same(diag):
        print(f"Player {diag[0]} is the winner diagonally(/)!")
        return True
    diag=[]
    for ix in range(len(game)):
        diag.append(game[ix][ix])

    if all_same(diag):
        print(f"Player {diag[0]} is the winner diagonally(\)!")
        return True
def game_Board(game_map,player=0,row=0,column=0,display=False):
    #if try throws exception or errors, except statements run 
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another!")
            return game_map,False
        print("   0  1  2")
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        print()
        return game_map, True
    #Code below prints when there is Index error, returns issue
    except IndexError:
        print("Error: make sure you input row/column as 0 1 or 2, " )
        return game_map,False
    #Code below runs when any other Exception is seen, returns issue
    except Exception as e:
        print(str(e))
        return game_map,False
def board_full(game):
    for row in game:
        if 0 in row:
            return False
        else:
            return True
play = True
players= [1,2]
while play:
    game=[[0,0,0],
        [0,0,0],
        [0,0,0]]
    game_won=False
    player_cycle=itertools.cycle([1,2])
    game,_ =game_Board(game, display=True)
    while not game_won:
        current_player = next(player_cycle)
        print(f"Player: {current_player}")
        played =False
        while not played:
            player_col = int(input("Which column? "))
            print()
            player_row = int(input("Which row? "))
            print()
            game, played= game_Board(game, player=current_player, row=player_row, column=player_col)
            dub=win(game)
        if dub or board_full(game):
            game_won=True
            if board_full(game) and not dub :
                print("Looks like its a tie!")
            again = input("Do you want to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() =="n":
                print("Good Game! Byeee")
                play=False
            else:
                print("Not a valid answer, so... bye bye")
                play=False

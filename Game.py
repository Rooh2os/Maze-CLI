import basic

player_cords = [0,0]

try:
    savedata = basic.json_read("savedata")
except(FileNotFoundError):
    savedata = [0,]

level = basic.json_read("levels/level_{savedata[1]}.json")

basic.clear
#air:0     1       3         2
print("Player: O\nWalls: #\nGoal: +")

row_ptr = 0
while row_ptr != 32:
    colum_ptr = 0
    while colum_ptr != 32:
        tile = level[row_ptr*32+colum_ptr]
        if tile == 0:
            print(" ",end="")
        elif tile == 1:
            print("O",end="")
        elif tile == 2:
            print("+",end="")
        else:
            print("#",end="")

        colum_ptr += 1
    print("")
    row_ptr += 1
basic.json_write("savedata",savedata,0)
import basic

player_cords = [0,0]

try:
    savedata = basic.json_read("savedata")
except(FileNotFoundError):
    savedata = [0,]

level = basic.json_read("levels/level_{leveln}.json")
basic.clear
#air:0     1       2         3
print("Player: O\nWalls: #\nGoal: +")


basic.json_write("savedata",savedata,0)
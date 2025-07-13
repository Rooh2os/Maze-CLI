import sys,math
sys.path.append("..")
import basic

#air:      Player:O       Goal:+        Wall:#         


while True:
    level = []
    leveltext = input("paste lvl txt (remove all new lines)\n")
    leveltext = leveltext.strip("\n")

    #level.append(input("player start x\n"))
    #level.append(input("player start y\n"))
    #level.append(input("player end x\n"))
    #level.append(input("player end y\n"))

    level.append(leveltext.index("O") % 33)
    level.append(math.floor(leveltext.index("O") / 32))
    level.append(leveltext.index("+") % 33)
    level.append(math.floor(leveltext.index("+") / 32))

    print(level[0])
    print(level[1])
    print(level[2])
    print(level[3])

    row_ptr = 0
    while row_ptr != 32:
        colum_ptr = 0
        while colum_ptr != 32:
            level.append(leveltext[row_ptr*32+colum_ptr])
            print(level[row_ptr*32+colum_ptr+4],end="")
            colum_ptr += 1
        print("")
        row_ptr += 1
    leveln = int(input("level number\n"))
    basic.json_write(f"../levels/level_{leveln}.json",level,0)
    
    if input("exit?\n") == "y":
        break
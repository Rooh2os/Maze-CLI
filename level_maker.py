import basic
#air:0     Player:1       Goal:2        Wall:3         

if input("myom") == "y":
    while True:
        level = []

        row_ptr = 0
        while row_ptr != 32:
            colum_ptr = 0
            while colum_ptr != 32:
                level.append(int(input("Intiger 0-3\n")))
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
            leveln = int(input("level number\n"))
            basic.json_write("/levels/level_{leveln}.json",level,0)
            if input("exit?") == "y":
                break
else:
    while True:
        level = []
        leveltext = input("paste lvl txt\n")
        row_ptr = 0
        while row_ptr != 32:
            colum_ptr = 0
            while colum_ptr != 32:
                level.append(leveltext[row_ptr*32+colum_ptr])
                tile = int(level[row_ptr*32+colum_ptr])
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
        leveln = int(input("level number\n"))
        basic.json_write(f"./levels/level_{leveln}.json",level,0)
        if input("exit?") == "y":
            break
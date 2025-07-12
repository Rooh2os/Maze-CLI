import random

lvl = ""

while len(lvl) != 32*32:
    if not("+" in lvl) and not("O" in lvl):
        lvl += random.choice("# +O")
    elif not("+" in lvl) and "O" in lvl:
        lvl += random.choice("# +")
    elif not("O" in lvl) and "+" in lvl:
        lvl += random.choice("# O")
    else:
        lvl += random.choice("# ")


#lvl = lvl.replace(" ","+",random.randint(0,lvl.count(" ")))
#lvl = lvl.replace(" ","O",1,random.randint(0,lvl.count(" ")))
print(lvl+"%")
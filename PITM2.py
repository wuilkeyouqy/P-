import time
def see_black(black):
  for i in black:
        PIM(i[0],i[1],'B')

def SEE_MAP(MAPB):
    for MX in MAPB:
        for MY in MX:
            print(MY,end = '')
        print()

def PIM(PLAYER_X,PLAYER_Y,THERE):
    PIM = MAP[PLAYER_X]
    PIM_Q = PIM[:PLAYER_Y]
    PIM_H = PIM[PLAYER_Y + 1:]
    PIM = PIM_Q + THERE + PIM_H
    MAP[PLAYER_X] = PIM

MAP =["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
      "X                    X       X         X     X",
      "X XXXXXX XX X X XXXXXXXXXX XXXXXXX XXXXXXXXX X",
      "X        XX  XX      XX XX XXXXXX  XXXXXX    X",
      "X XXXXXXXMX XXXX X     X           X X   X   X",
      "X X   X   XXXX    X    X        X      X     X",
      "X   X   XX   XX   X XXXXXXXXX XXXXXXXXXXXXXX X",
      "X XXXXXXX   X   XXX     XXXX    XXXXXX X X X X",
      "X            XXXXX  XX       XX              X",
      "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",]
NUMBER_X,NUMBER_Y = 10,4
PX,PY,SP = 3,8,'P' #player
JPX,JPY = PX,PY
MX,MY,SM = 4,9,'M' #there
BLACK_LIST = []
RED_LIST = []
a = 0
RED_LIST.append([PX,PY])
JC=True
a = 0
while MX - PX != 0 or MY - PY != 0:
    #see_black(BLACK_LIST)
    a += 1
    time.sleep(0.1)
    PIM(MX,MY,SM)
    JPX,JPY = PX,PY
    PIM(PX,PY,SP)
    SEE_MAP(MAP)
    if (MX - PX < 0) and (MAP[PX-1][PY] != 'X') and not([PX-1,PY] in BLACK_LIST) and not([PX-1,PY] in RED_LIST):
        PX -= 1
    elif (MY - PY > 0) and (MAP[PX+1][PY] != 'X') and not([PX+1,PY] in BLACK_LIST) and not([PX+1,PY] in RED_LIST):
        PX +=1
    elif (MY - PY < 0) and (MAP[PX][PY-1] != 'X') and not([PX,PY-1] in BLACK_LIST) and not([PX,PY-1] in RED_LIST):
        PY -= 1
    elif (MY - PY > 0) and (MAP[PX][PY+1] != 'X') and not([PX,PY+1] in BLACK_LIST) and not([PX,PY+1] in RED_LIST):
        PY += 1
    else:
        if (MAP[PX-1][PY] != 'X') and not([PX-1,PY] in BLACK_LIST) and not([PX-1,PY] in RED_LIST):
            PX -= 1
        elif (MAP[PX+1][PY] != 'X') and not([PX+1,PY] in BLACK_LIST) and not([PX+1,PY] in RED_LIST):
            PX +=1
        elif (MAP[PX][PY-1] != 'X') and not([PX,PY-1] in BLACK_LIST) and not([PX,PY-1] in RED_LIST):
            PY -= 1
        elif (MAP[PX][PY+1] != 'X') and not([PX,PY+1] in BLACK_LIST) and not([PX,PY+1] in RED_LIST):
            PY += 1
        else:
            BLACK_LIST.append([PX,PY])
            PIM(JPX,JPY,' ')
            if JC:
                BED = RED_LIST[-1]
                PX = BED[0]
                PY = BED[1]
                JC = not(JC)
                continue
            else:
                BED = RED_LIST[-2]
                PX = BED[0]
                PY = BED[1]             
                JC = not(JC)
                RED_LIST = RED_LIST[:-2]
                
    
    RED_LIST.append([PX,PY])        
    PIM(JPX,JPY,' ')
print(a // (len(MAP) * 88),end = '')
print(f'%---{a}')
print("结束")

    
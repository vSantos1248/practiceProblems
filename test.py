def bishopAndPawn(bishop, pawn):
    pawn=[ord(pawn[0])-97, int(pawn[1])-1];
    bishop=[ord(bishop[0])-97, int(bishop[1])-1];
    #print("original bishop, pawn:", bishop, pawn);
    

    if(checkTopLeft(bishop, pawn)): return True;
    if(checkTopRight(bishop,pawn)): return True;
    if(checkBottomLeft(bishop,pawn)): return True;
    if(checkBottomRight(bishop,pawn)): return True;
    return False;

def checkTopLeft(b,p):
    while(b[0]>-1 and b[1]<8):
        b[0]-=1;
        b[1]+=1;
        if(b==p): return True;
    return False;

def checkTopRight(b,p):
    while(b[0]<8 and b[1]<8):
        ##print("inside of topRight:", b,p);
        b[0]+=1;
        b[1]+=1;
        if(b==p): return True;
    return False;
    
def checkBottomLeft(b,p):
    while(b[0]>-1 and b[1]>-1):
        b[0]-=1;
        b[1]-=1;
        if(b==p): return True;
    return False;

def checkBottomRight(b,p):
    while(b[0]<8 and b[1]>-1):
        b[0]+=1;
        b[1]-=1;
        if(b==p): return True;
    return False;

bishopAndPawn("a1","c3");

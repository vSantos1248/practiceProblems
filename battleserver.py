#https://github.com/dutc/battlegame

class Battleserver:
    def __init__(self, length=8, height=8, randomize=True):
        from random import randint;
        self.length=length;
        self.height=height;
        self.board=[[0]*length]*height;
        self.carrierHP=0;
        self.battleshipHP=0;
        self.cruiserHP=0;
        self.submarineHP=0;
        self.destroyerHP=0;
        
        if randomize:
            if randint(0,1)==0: #set carrier
                setShip=False;
                self.carrierHP=5;
                
                if randint(0,1)==0 and length>4: #build horizontally
                    x=randint(0,length-1-5);
                    y=randint(0,height-1);
                    
                else: #build vertically

from random import randint;
for i in range(10):
    print(randint(0,1));


import random
#parent class
class human:
    counter=-1
    def __init__(self) :
        pass
    def get_name(self):
        #TODO:this will return a name for every objects
        random.seed()
        names=['حسین','مازیار','اکبر','نیما','مهدی' 
            ,'فرهاد','محمد','خشایار','میلاد','مصطفی', 
            'امین','سعید','پویا','پوریا','رضا','علی', 
            'بهزاد','سهیل','بهروز','شهروز','سامان','محسن']
        human.counter+=1
        return names[human.counter]      
      
class footbalist(human):
    playercounter=0
    #TODO:this will hold the player name and their teams
    playerArrange=dict()
    #TODO:this will arange the players in teams
    def __init__(self,playername):
        super().__init__()
        self.player=playername
    def arrenge_team(self):
        random.seed()
        teamrandom=random.randrange(0,1)
        if(teamrandom==0 and footbalist.playercounter<11):
            footbalist.playerArrange[self.player]='TeamA'
            footbalist.playercounter+=1
        else:
            footbalist.playerArrange[self.player]='TeamB'
            footbalist.playercounter+=1    
           
    def printArange(self):
        for i in footbalist.playerArrange.items():
            #print(i[0],i[1])
            #print(i[0],' -> ',i[1])
            print('%3s : %-5s' %(i[1],i[0]))
 
player=human()
for i in range(22):
    #TODO:this will get name from parent class
    PlayerName=player.get_name()
    #TODO:this will arage player in teams 
    PlayerName=footbalist(PlayerName)
    PlayerName.arrenge_team()
    if(i==21):
        PlayerName.printArange()  
   

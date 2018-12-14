 '''
Katie Naughton
Programming Final Proj
Sources:
check collisions, change score, then call the change score def 
'''
from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class House1(Sprite):
    
    h1_asset = ImageAsset("images/Christmas_Gingerbread_House_PNG_Clipart.png")
    def __init__(self, position):
        super().__init__(House1.h1_asset, position)
        self.scale=0.3
        self.vx=-2
    
    def step(self):
        self.x+=self.vx
        if self.x<=-800:
            self.x=myapp.width
        
class House2(Sprite):
    
    h2_asset = ImageAsset("images/christmas-clipart-with-house-11.png")
    def __init__(self, position):
        super().__init__(House2.h2_asset, position)
        self.scale=0.2
        self.vx=-2
    
    def step(self):
        self.x+=self.vx
        if self.x<=-800:
            self.x=myapp.width

class Grinch(Sprite):
    
    g_asset = ImageAsset("images/clipart975771.png")
    def __init__(self, position):
        super().__init__(Grinch.g_asset, position)
        self.scale=0.25
        self.vx=-1.5
    
    def step(self):
        self.x+=self.vx
        if self.x<=-800:
            self.x=myapp.width

class Present1(Sprite):
    
    p1_asset = ImageAsset("images/clipart42143.png")
    def __init__(self, position):
        super().__init__(Present1.p1_asset, position)
        self.scale=0.1
        self.vy=0
        self.a=0
        SantaGame.listenMouseEvent("click", self.MouseClick)
        self.visible=True
      
    def MouseClick (self, event):
        self.vy=0
        self.a=0.13
    

    def step(self):
        self.vy+=self.a
        self.y+=self.vy
        
        self.collision=self.collidingWithSprites(House1) or self.collidingWithSprites(House2)
        
        if self.visible and (self.collision) or self.y>800:
            self.x=350
            self.y=50
            self.vy=0
            self.a=0
            
        totalscore=0
        s_asset=TextAsset(("Presents Delivered: {0}!! :)").format(totalscore), width=500, align='left',style='30px Arial', fill=Color(0xff2222,1))
        if self.visible and self.collision: 
            totalscore+=1
            Score.scoreChange()
            
            
        #if self.visible and self.collidingWithSprites(Grinch):
            #myapp.hearts.removeheart()
            
class Score(Sprite):
    def __init__(self):
    pass

    # Sprite(TextAsset(equation, width=100, align='center',style='12px Arial', fill=black),(5,(len(self.functions)-1)*frameHeight/20+2))
    scores = []
    def scoreChange():
        shift = 0
        for i in range(len(Score.scores)):
            i = i - shift
            Score.scores[i].destroy()
            del Score.scores[i]
            shift += 1
        s_asset=TextAsset(("Your score is {0}").format(Present1.totalscore), width=500, align='center',style='12px Arial', fill=Color(0x000000,1))
        Score.scores.append(Sprite(s_asset, (0,0)))
 
  

        
        
    '''   
class Heart(Sprite):
    
    heart_asset = ImageAsset("images/heart.png")
    def __init__(self, position):
        super().__init__(Heart.heart_asset, position)
        self.scale=1
        
class Heartlist():
    
    def __init__(self):
        self.heartlist=[Heart((300+(i*20),350)) for i in range(5)]
        self.count = 5
        
    def removeheart(self):
        if self.count >= 0:
            self.count -= 1
            self.heartlist[self.count].visible = False
        elif self.count<=0:
            self.text=Sprite(TextAsset("GAME OVER:( your heart shrunk two sizes too small!", width=500, align='center',style='60px Arial', fill=Color(0xff2222,1)), (300,350))
       '''
       
class Background(Sprite):
    
    bg_asset = ImageAsset("images/83581c872f38421.jpg")
    def __init__(self, position):
        super().__init__(Background.bg_asset, position)
        self.scale=0.78788
        self.vx=-1.5
    
    def step(self):
        self.x+=self.vx
        if self.x<=-513:
            self.x+=self.width*3
        
class SantaGame(App):
    
    def __init__(self):
        super().__init__()
       
        #initial positions
        Background((0,0))
        Background((512,0))
        Background((1024,0))
        House1((500,350))
        House2((900,350))
        Grinch((2500, 335))
        self.p1=Present1((350,50))
        
        #hearts
        #self.hearts = Heartlist()
        #self.hearts.removeheart()
        
        #sleigh
        sleigh_asset=ImageAsset("images/santa_sleigh_PNG72.png")
        sleigh=Sprite(sleigh_asset, (350, 50))
        sleigh.scale=0.3
        
        #music
        jingle_asset = SoundAsset("sounds/Santa Claus Is Coming To Town.mp3")
        jingle=Sound(jingle_asset)
        jingle.volume=8
        jingle.play()
        
    
      
        
    def step(self):
        for house1 in self.getSpritesbyClass(House1):
            house1.step()
        for house2 in self.getSpritesbyClass(House2):
            house2.step()
        for g in self.getSpritesbyClass(Grinch):
            g.step()
        for p1 in self.getSpritesbyClass(Present1):
            p1.step()
        for score in self.getSpritesbyClass(Score):
            score.step()
        for bg in self.getSpritesbyClass(Background):
            bg.step()
       
myapp=SantaGame()
myapp.run()



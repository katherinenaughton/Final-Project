'''
Katie Naughton
Programming Final Proj
Sources:

QUESTIONS: lives/hearts how to access the list when creating positions?
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
        if self.visible and (self.collidingWithSprites(House1) or self.collidingWithSprites(House2)) or self.y>800:
            self.x=350
            self.y=50
            self.vy=0
            self.a=0
            
        h1score=[]
        if self.collidingWithSprites(House1):
            h1score.append("a")
        print(h1score)
        scorea= len(h1score)
        print(scorea)
        
        h2score=[]
        if self.collidingWithSprites(House2):
            h2score.append("b")
        print(h2score)
        scoreb= len(h2score)
        print(scoreb)
        
        
        totalscore=scorea + (2*score b)
        
            
        
            
class Heart(Sprite):
    
    heart_asset = ImageAsset("images/heart.png")
    def __init__(self, position):
        super().__init__(Heart.heart_asset, position)
        self.scale=1
        
class Heartlist():
    
    def __init__(self):
       
        heartlist=[Heart((300+(i*20),350)) for i in range(5)]
        H=heartlist[0]
        H1=heartlist[1]
        H2=heartlist[2]
        H3=heartlist[3]
        H4=heartlist[4]
        
        
        
        
       
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
        House1((350,350))
        House2((1200,350))
        Grinch((2500, 335))
        Present1((350,50))
        Heartlist(H)
        Heartlist(H1)
        Heartlist(H2)
        Heartlist(H3)
        Heartlist(H4)
       
        #sleigh
        sleigh_asset=ImageAsset("images/santa_sleigh_PNG72.png")
        sleigh=Sprite(sleigh_asset, (350, 50))
        sleigh.scale=0.3
        
        #music
        jingle_asset = SoundAsset("sounds/Santa Claus Is Coming To Town.mp3")
        jingle=Sound(jingle_asset)
        jingle.volume=8
        jingle.play()
        
        #scoreboard
        self.text=Sprite(TextAsset("GAME OVER :(", width=500, align='center',style='60px Arial', fill=Color(0xff2222,1)), (300,350))
        self.text.visible= False
        
    def step(self):
        for house1 in self.getSpritesbyClass(House1):
            house1.step()
        for house2 in self.getSpritesbyClass(House2):
            house2.step()
        for g in self.getSpritesbyClass(Grinch):
            g.step()
        for p1 in self.getSpritesbyClass(Present1):
            p1.step()
        for heart in self.getSpritesbyClass(Heart):
            heart.step()
        for heartl in self.getSpritesbyClass(Heartlist):
            heartl.step()
        for bg in self.getSpritesbyClass(Background):
            bg.step()
       
myapp=SantaGame()
myapp.run()











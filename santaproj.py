'''
Katie Naughton
Programming Final Proj
Sources: Noah, Mr. Dennison
'''
print( "Click the mouse to drop a present! Try to hit the presents! Don't hit the Grinchs!")
from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class House1(Sprite):
    
    h1_asset = ImageAsset("images/Christmas_Gingerbread_House_PNG_Clipart.png")
    def __init__(self, position):
        super().__init__(House1.h1_asset, position)
        self.scale=0.3
        self.vx=-6
    
    def step(self):
        self.x+=self.vx
        if self.x<=-800:
            self.x=myapp.width
        
class House2(Sprite):
    
    h2_asset = ImageAsset("images/christmas-clipart-with-house-11.png")
    def __init__(self, position):
        super().__init__(House2.h2_asset, position)
        self.scale=0.2
        self.vx=-6
    
    def step(self):
        self.x+=self.vx
        if self.x<=-800:
            self.x=myapp.width

class Grinch(Sprite):
    
    g_asset = ImageAsset("images/clipart975771.png")
    def __init__(self, position):
        super().__init__(Grinch.g_asset, position)
        self.scale=0.25
        self.vx=-6
    
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
    totalscore=0
      
    def MouseClick (self, event):
        self.vy=0
        self.a=0.9
    

    def step(self):
        self.vy+=self.a
        self.y+=self.vy
        
        self.collision=self.collidingWithSprites(House1) or self.collidingWithSprites(House2)
        self.gcollision=self.collidingWithSprites(Grinch)
        
        if self.visible and (self.collision or self.gcollision) or self.y>800:
            self.x=350
            self.y=50
            self.vy=0
            self.a=0
            
            
    
        #s_asset=TextAsset(("Presents Delivered: {0}!! :)").format(totalscore), width=500, align='left',style='30px Arial', fill=Color(0xff2222,1))
        if self.visible and self.collision: 
            self.totalscore+=1
            #print(self.totalscore)
            Score.scoreChange(self.totalscore)
        
        
        if self.visible and self.gcollision:
            myapp.Hlist.removeheart()
            
class Score(Sprite):
    
    scores = []
    def scoreChange(totalscore):
        #print(Present1.totalscore)
        shift = 0
        for i in range(len(Score.scores)):
            i = i - shift
            Score.scores[i].destroy()
            del Score.scores[i]
            shift += 1
        s_asset=TextAsset(("Presents Delivered: {0}!!").format(totalscore), width=500, align='left',style='30px Arial', fill=Color(0xff222,1))
        Score.scores.append(Sprite(s_asset, (0,0)))
        
 
class Heart(Sprite):
    
    heart_asset = ImageAsset("images/heart.png")
    def __init__(self, position):
        super().__init__(Heart.heart_asset, position)
        self.scale=0.1
        
class Heartlist():
    
    def __init__(self):
        self.count = 3
        self.heartlist=[Heart((0+(i*40),50)) for i in range(3)]
    
    def removeheart(self):
        if self.count >= 0:
            self.count -= 1
            self.heartlist[self.count].destroy()
        if self.count<=0:
            self.text=Sprite(TextAsset("GAME OVER:( your heart shrunk two sizes too small!", width=1000, align='center',style='30px Arial', fill=Color(0xff2222,1)), (100,150))
            myapp.gameover=True

class Background(Sprite):
    
    bg_asset = ImageAsset("images/83581c872f38421.jpg")
    def __init__(self, position):
        super().__init__(Background.bg_asset, position)
        self.scale=0.78788
        self.vx=-5.5
    
    def step(self):
        self.x+=self.vx
        if self.x<=-513:
            self.x+=self.width*3
        
class SantaGame(App):
    
    def __init__(self):
        super().__init__()
        
        self.gameover=False
       
        #initial positions
        Background((0,0))
        Background((512,0))
        Background((1024,0))
        House1((300,350))
        House2((900,350))
        Grinch((1000, 335))
        Grinch((100,335))
        Grinch((1500,335))
        self.p1=Present1((350,50))
        self.Hlist = Heartlist()
        
      
        
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
        if self.gameover:
            return
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









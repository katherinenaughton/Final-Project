'''
Katie Naughton
Programming Final Proj
Sources:
'''


from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class House1(Sprite):
    
    h1_asset = ImageAsset("images/Christmas_Gingerbread_House_PNG_Clipart.png")
    def __init__(self, position):
        super().__init__(House1.h1_asset, position)
        self.scale=0.3
        self.vx=-1.5
    
    def step(self):
        self.x+=self.vx
        if self.x<=-800:
            self.x=myapp.width
        
    
class House2(Sprite):
    
    h2_asset = ImageAsset("images/christmas-clipart-with-house-11.png")
    def __init__(self, position):
        super().__init__(House2.h2_asset, position)
        self.scale=0.2
        self.vx=-1.5
    
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
        self.visible=True
        SantaGame.listenMouseEvent("click", self.MouseClick)
    
    def MouseClick (self, event):
        self.vy=1
    
    def step(self):
        self.y+=self.vy
         if self.visible and (self.collidingWithSprites(House1) or self.collidingWithSprites(House2)):
            self.visible=False

        

class Background(Sprite):
    
    bg_asset = ImageAsset("images/83581c872f38421.jpg")
    def __init__(self, position):
        super().__init__(Background.bg_asset, position)
        self.scale=0.78788
        self.vx=-1
    
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
       
        #sleigh
        sleigh_asset=ImageAsset("images/santa_sleigh_PNG72.png")
        sleigh= Sprite(sleigh_asset, (350, 50))
        sleigh.scale=0.3
        
        #Music:Santa Claus is Coming to Town
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
        for bg in self.getSpritesbyClass(Background):
            bg.step()
       
        


myapp=SantaGame()
myapp.run()







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
        
    
class House2(Sprite):
    
    h2_asset = ImageAsset("images/20-204688_gingerbread-house-cliparts-christmas-gingerbread-house-clipart.png")
    def __init__(self, position):
        super().__init__(House2.h2_asset, position)
        self.scale=0.3
        self.vx=-1.5
    
    def step(self):
        self.x+=self.vx
        
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
        House2((500,350))
       
        
        
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
        for bg in self.getSpritesbyClass(Background):
            bg.step()
        



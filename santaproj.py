'''
Katie Naughton
Programming Final Proj
Sources:
'''

from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class House1(Sprite):
    
    h1_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
   
   
    
    def __init__(self, position):
        super().__init__(House1.h1_asset, position)
        
class SantaGame(App):
    
    
    def __init__(self):
        super().__init__()
        
        #background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/83581c872f38421.jpg")
        bg = Sprite(bg_asset, (0,-200))
        bg.scale=1.4
        
        #sleigh
        sleigh_asset=ImageAsset("images/santa_sleigh_PNG72.png")
        sleigh= Sprite(sleigh_asset, (350, 100))
        sleigh.scale=0.3
        
        #JingleBells
        jingle_asset = SoundAsset("sounds/Santa Claus Is Coming To Town.mp3")
        jingle=Sound(jingle_asset)
        jingle.volume=8
        jingle.play()

        

myapp = SantaGame()

myapp.run()

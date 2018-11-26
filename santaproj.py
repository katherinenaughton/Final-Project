'''
Katie Naughton
Programming Final Proj
Sources:
'''

from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class Santa(App):
    
    def __init__(self):
        super().__init__()
        
        #background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/83581c872f38421.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale=1.4
        
        #sleigh
        sleigh_asset=ImageAsset("images/santa_sleigh_PNG72.png")
        sleigh= Sprite(sleigh_asset, (350, 100))
        sleigh.scale=0.3

myapp = Santa()

myapp.run()

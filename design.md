# Santa Game

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. https://runpython.org or ggame)?
I used runpython.org and ggame. 
* What language will you use for coding (usually Python 3)?
I used Python 3. 
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?

The classes I use in my program and their functions are as follows: 

House1 
This creates the first House Sprite, and sets its velocity and scale. It moves the house backwards so it looks like the sleigh is moving forward, and when it hits the edge of the screen, it resets to the other side. 

House2
House 2 does the same exact thing as House 1, but it is a different image. 

Grinch 
The Grinch class does the same thing as House1 and House2. 

Present1
Here's where a lot of the action happens. The present class will drop a present if the mouse is clicked. It also checks for collisions with both house classes and the grinch class. The present has its own acceleration, and once it hits the ground, house or grinch it resets back into the sleigh. This class also calls the scorechange function if a collision with a present is detected, and the removeheart function if a collision with the grinch occurs. 

Score
This score class controls the scoreboard for the total number of presents is delivered. It defines the scorechange function. Once a present hits a house, the old textasset is destroyed, and a new one is created with the new score. 

Heart
This class creates the heart image. 

Heartlist
This class creates a list of hearts, and defines the remove heart function which removes a heart when a grinch is hit. When there are no hearts left, a game over textasset is displayed. 

Background
This class creates the "continous" and moving background. Three bakcground image assets are overlapped, and when one goes over the edge, it resets to the other side. 

SantaGame
The App class creates the game. It defines the positions of all the assets, creates Santa's sleigh, and also plays music. It finally calls the step functions. 

# BOMBERMAN
#### By: Syed Mohd Ali Rizwi


Bomberman - A fun game written in python.


##### Prerequisites:
* python/python3
* termcolor


Run the game by executing any of the following commands:

``` python3 bomberman.py ``` or ``` python bomberman.py```


##### Basic Controls :--

  Function     key

* Move left 	a 
* Move right	d 
* Move up   	w 
* Move down 	s 
* Drop bomb 	b
* Quit		q 


##### Representation:

'/' represents Bricks
'B' represents Bomberman 
'E' represents Enemy
'e' represents the fire of explosion
'X' The walls


##### Functionality:

* The player is controlled by the user and the enemies move randomly on the board but cannot walk through walls or bricks.
* Bomberman can drop a bomb which destroys bricks and enemies around it after 3 seconds .On killing an enemy, user scores 100 points and on breaking bricks user scores 20 points.
* There are 3 levels of the game. On killing all the enemies, level is incremented increasing the difficulty of the game.
* User win the game on passing all the levels.


##### Implementation:

It is implemented in python following the OOP's Principles.
Bonus Part:
* The bomb displays the number of seconds left for explosion instead of ‘O’. For example if one second is left then  
  1111   =>    0000  => explosion 
  1111         0000 
* Different objects have different coloured symbols i.e.'E'(enemies) are of RED colour ,'/'(bricks) are of GREEN colour, 'X'(walls) are of BLUE colour.
* Extra levels are implemented with different difficulty level.






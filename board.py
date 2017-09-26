from __future__ import print_function
import signal,copy,sys,time
from random import randint

gameArray = [[0 for x in range(80)] for y in range(40)]
class Board():

	def gameBoard(self):
		
		gameArray[0][0]=1
		for i in range(1,39):
			for j in range(1,77):
					if ( i<3 or i>36 ):
						gameArray[i][j] = "X"
					elif ( j<5 or j>72 ):
						gameArray[i][j] = "X"
					elif ( (i>4 and i<36 and j<73 and j>8) and (i%4==1 or i%4==2) and (j%8==1 or j%8==2 or j%8==3 or j%8==4)):
						gameArray[i][j] = "X"
					else:
						gameArray[i][j] = " "
		return gameArray


	
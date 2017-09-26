from __future__ import print_function
import signal,copy,sys,time
from random import randint
from termcolor import colored
from board import *
from brick import *
from person import *
from player import *
from enemy import *
from bomb import *

bo = Board()
br = Brick()
pl = Player()
en = Enemy()
bom = Bomb()

class Gameplay():
	def __init__(self):
		self.cur_time = time.time()


	def printboard(self):

		gameArray = bo.gameBoard()
		br.drawBricks()
		pl.updatePlayer()

		run_time = time.time() - self.cur_time
		if(run_time > 1):
			en.updatePos()
			self.cur_time = time.time()
		else:
			en.drawEnemy()

		
		if(run_time > 1 and bomPos[2] >= 0):
			bom.drawBomb()
		
		for i in range(1,39):
			for j in range(1,77):
				if(gameArray[i][j]=="X"):
					print(colored(gameArray[i][j],"blue"),end="")
				elif(gameArray[i][j]=="E"):
					print(colored(gameArray[i][j],"red"),end="")
				elif(gameArray[i][j]=="/"):
					print(colored(gameArray[i][j],"green"),end="")
			
				elif bimbo and [i,j] in bimbo:
					print(bomPos[2],end="")
				else:
					print(gameArray[i][j],end="")
			print("\n",end="")
		print("Press 'q' to quit the game")	

		return


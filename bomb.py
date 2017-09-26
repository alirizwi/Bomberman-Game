from __future__ import print_function
import signal,copy,sys,time
from random import randint
from board import *
from player import *
from enemy import *
from brick import *

bomPos = [0,0,-1]
bombThrown = 0
bimbo=[]
pl = Player()
en = Enemy()

class Bomb():

	def drawBomb(self):
		x = bomPos[0]
		y = bomPos[1]
		#print(bomPos[0],bomPos[1],bomPos[2])

		if(bomPos[2] > -1):
			if not bimbo:
				for i in range(1,3):
					for j in range(1,5):

						bimbo.append([2*x+i,4*y+j])

			gameArray[2*x+1][4*y+1] = bomPos[2]
			gameArray[2*x+1][4*y+2] = bomPos[2]
			gameArray[2*x+1][4*y+3] = bomPos[2]
			gameArray[2*x+1][4*y+4] = bomPos[2]
			gameArray[2*x+2][4*y+1] = bomPos[2]
			gameArray[2*x+2][4*y+2] = bomPos[2]
			gameArray[2*x+2][4*y+3] = bomPos[2]
			gameArray[2*x+2][4*y+4] = bomPos[2]
		bomPos[2] -= 1
		if(bomPos[2] == -1):
			self.explosion()
		return

	def drawExplosion(self,x,y):

		gameArray[2*x+1][4*y+1] = "e"
		gameArray[2*x+1][4*y+2] = "e"
		gameArray[2*x+1][4*y+3] = "e"
		gameArray[2*x+1][4*y+4] = "e"
		gameArray[2*x+2][4*y+1] = "e"
		gameArray[2*x+2][4*y+2] = "e"
		gameArray[2*x+2][4*y+3] = "e"
		gameArray[2*x+2][4*y+4] = "e"		
		return

	def afterExplosion(self,x,y):

		if(x == playerPos[0] and y == playerPos[1]):
		#	print("pakad gya")
			pl.updateLife()

		if(enemyNum>0 and [x,y] in enemyPos):
			enemyPos.remove([x,y])
			pl.updateScore(100)
			en.updateNum(-1)

		if([x,y] in brickPos):
			brickPos.remove([x,y])
			pl.updateScore(20)	

		bimbo[:]=[]
		return

	def checkPos(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="X" ):
			return -1
		return 1


	def explosion(self):
		x = bomPos[0]
		y = bomPos[1]
		self.drawExplosion(x,y)
		self.afterExplosion(x,y)

		if(self.checkPos(x-1,y)>0):
			self.drawExplosion(x-1,y)
			self.afterExplosion(x-1,y)

		if(self.checkPos(x+1,y)>0):
			self.drawExplosion(x+1,y)
			self.afterExplosion(x+1,y)

		if(self.checkPos(x,y-1)>0):
			self.drawExplosion(x,y-1)
			self.afterExplosion(x,y-1)

		if(self.checkPos(x,y+1)>0):
			self.drawExplosion(x,y+1)
			self.afterExplosion(x,y+1)
		return



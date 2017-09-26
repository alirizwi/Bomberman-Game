from __future__ import print_function
import signal,copy,sys,time
from random import randint
from person import * 
from board import *

playerPos = [1,1]
score = 0
lives = 3

class Player(Person):

	def drawPlayer(self,x,y):
		if(gameArray[2*x+1][4*y+1]!="X" and gameArray[2*x+1][4*y+1]!="/"):
				gameArray[2*x+1][4*y+1] = "B" 
				gameArray[2*x+1][4*y+2] = "B"
				gameArray[2*x+1][4*y+3] = "B"
				gameArray[2*x+1][4*y+4] = "B"
				gameArray[2*x+2][4*y+1] = "B" 
				gameArray[2*x+2][4*y+2] = "B"
				gameArray[2*x+2][4*y+3] = "B"
				gameArray[2*x+2][4*y+4] = "B"
		return

	def checkPos(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="/"):
			return -1
		return 1

	def checkEnemy(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="E"):
			return -1
		return 1	

	def updatePlayer(self):
		x = playerPos[0]
		y = playerPos[1]
		self.drawPlayer(x,y)
		if(lives <= 0):
			print("Game Over")
			print("Score:",score)
			sys.exit(1)

		print("Score      :",score,"\t\t\t\t\t\t","Lives left :",lives)
		#print("Lives left :",lives)
		return		

	def playerInit(self):
		playerPos[0] = 1
		playerPos[1] = 1
		x = playerPos[0]
		y = playerPos[1]
		return

	def moveDown(self):
		x = playerPos[0]
		y = playerPos[1]
		if(self.checkEnemy(x+1,y)>0):
			if(self.checkPos(x+1,y)>0):
				playerPos[0] += 1
				self.drawPlayer(playerPos[0],playerPos[1])
		else:
			self.updateLife()
		return

	def moveUp(self):
		x = playerPos[0]
		y = playerPos[1]	
		if(self.checkEnemy(x-1,y)>0):
			if(self.checkPos(x-1,y)>0):
				playerPos[0] -= 1
				self.drawPlayer(playerPos[0],playerPos[1])
		else:
			self.updateLife()	
		return

	def moveLeft(self):
		x = playerPos[0]
		y = playerPos[1]		
		if(self.checkEnemy(x,y-1)>0):
			if(self.checkPos(x,y-1)>0):
				playerPos[1] -= 1
				self.drawPlayer(playerPos[0],playerPos[1])
		else:
			self.updateLife()
		return

	def moveRight(self):
		x = playerPos[0]
		y = playerPos[1]		
		if(self.checkEnemy(x,y+1)>0):
			if(self.checkPos(x,y+1)>0):
				playerPos[1] += 1
				self.drawPlayer(playerPos[0],playerPos[1])
		else:
			self.updateLife()
		return

	def updateScore(self, update):
		global score
		score += update
		return 

	def updateLife(self):
		global lives
		lives -= 1
		playerPos[0] = 1
		playerPos[1] = 1
		return
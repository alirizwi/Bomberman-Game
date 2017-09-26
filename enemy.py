from __future__ import print_function
import signal,copy,sys,time
from random import randint
from person import * 
from board import *
from person import *
from player import *

enemyPos = []
enemyNum = 5
pl = Player()

class Enemy(Person):

	def drawEnemy(self):
		x = len(enemyPos)
		for i in range(x):
			x = enemyPos[i][0]
			y = enemyPos[i][1]
			#print("x and y",x,y)
			if(gameArray[2*x+1][4*y+1]!="X" and gameArray[2*x+1][4*y+1]!="/"):
					gameArray[2*x+1][4*y+1] = "E" 
					gameArray[2*x+1][4*y+2] = "E"
					gameArray[2*x+1][4*y+3] = "E"
					gameArray[2*x+1][4*y+4] = "E"
					gameArray[2*x+2][4*y+1] = "E" 
					gameArray[2*x+2][4*y+2] = "E"
					gameArray[2*x+2][4*y+3] = "E"
					gameArray[2*x+2][4*y+4] = "E"
		return

	def checkPos(self,x,y):
		if(gameArray[2*x+1][4*y+1]=="X" or gameArray[2*x+2][4*y+1]=="X" or gameArray[2*x+1][4*y+1]=="/" or gameArray[2*x+2][4*y+1]=="/"):
			return -1
		return 1	

	def enemyInit(self):
		for i in range(enemyNum):
			x = randint(1,17)
			y = randint(1,17)	
			enemyPos.append([x,y])
			print(enemyPos[i][0],enemyPos[i][1])
		self.drawEnemy()
		return

	def killPlayer(self,x,y):
		pl.updateLife()
		return

	def updatePos(self):
		x = len(enemyPos)
		#print(x)
		for i in range(x):
			#print("i=",i)
			x = enemyPos[i][0]
			y = enemyPos[i][1]
			#print("x=",x,"y=",y)
			if(x == playerPos[0] and y == playerPos[1]):
				self.killPlayer(x,y)
			if(x<18 and y<18):
				dir = randint(1,4)
				if(dir == 1):
					if(self.checkPos(x-1,y)>0):
						
						if(x-1 == playerPos[0] and y == playerPos[1]):
							self.killPlayer(x-1,y)
						enemyPos[i][0] -= 1
						
				elif(dir == 2):
					if(self.checkPos(x+1,y)>0):
						
						if(x+1 == playerPos[0] and y == playerPos[1]):
							self.killPlayer(x+1,y)
						enemyPos[i][0] += 1
						
				elif(dir == 3):
					if(self.checkPos(x,y-1)>0):
						
						if(x == playerPos[0] and y-1 == playerPos[1]):
							self.killPlayer(x,y-1)
						enemyPos[i][1] -= 1
						
				elif(dir == 4):
					if(self.checkPos(x,y+1)>0):
						
						if(x == playerPos[0] and y+1 == playerPos[1]):
							self.killPlayer(x,y+1)
						enemyPos[i][1] += 1
					
		self.drawEnemy()
		return

	def updateNum(self,val):
		global enemyNum
		enemyNum += val
		print("enemy:",enemyNum)
		return

	def enNum(self):
		return enemyNum

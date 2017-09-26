from __future__ import print_function
import signal,copy,sys,time
from random import randint
import os
from gameplay import *
from getchunix import *
from person import *
from player import *
from bomb import *
from brick import *
from alarmexception import *

getch = GetchUnix()

def alarmHandler(signum, frame):
    raise AlarmException

def input_char(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

g=Gameplay()
pl = Player()
bom = Bomb()
br = Brick()
pl.playerInit()
en.enemyInit()
br.brickInit()
level = 1

while(1):
	os.system("tput reset")
	enemyNum = en.enNum()
	if(enemyNum == 0 and level <= 3):
		level += 1
		en.updateNum(5*level)
		en.enemyInit()
	print("Level      :",level)
	g.printboard()		#prints the game-board
	inp = input_char()	#takes a single character input from keyboard
	if(inp == 'q'):
		sys.exit(0)		#Quits
	elif(inp == 's'):
		pl.moveDown()	#moves the player down on pressing 's'
	elif(inp == 'w'):
		pl.moveUp()		#moves the player up on pressing 'w'
	elif(inp == 'a'):
		pl.moveLeft()	#moves the player left on pressing 'a'
	elif(inp == 'd'):
		pl.moveRight()	#moves the player right on pressing 'd'
	elif(inp == 'b'):	#spawn a bomb on pressing 'b'
		if(bomPos[2] == -1):
			bomPos[0] = playerPos[0]
			bomPos[1] = playerPos[1]
			bomPos[2] = 3
			bom.drawBomb()

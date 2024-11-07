
import os
from utils import randcell

class Helicopter:
	def __init__(self,w,h):
		rc=randcell(w,h) #первая клетка ветралёта
		rx, ry=rc[0],rc[1]
		self.x=rx
		self.y=ry
		self.h=h
		self.w=w
		self.mxtant=1 #максимальная ёмкасть резервуара
		self.tant=0 #текущая ёмкасть резервуара
		self.score=0
		self.lives=20

	def move(self,dx,dy):
		nx=self.x+dx
		ny=self.y+dy
		if nx>=0 and ny>=0 and nx<self.h and ny<self.w:
			self.x,self.y=nx,ny

	def print_stels (self):
		print('% ',self.tant,'/',self.mxtant,sep="",end='|')
		print('Очки:',self.score,end='|')
		print('L:',self.lives)

	def game_over(self):
		os.system("cls")
		print('##########################')
		print('     GAME OVER     SCORE',self.score)
		print('##########################')	
		exit(0)

	def export_data(self):
		return {'lives':self.lives,
				'score':self.score,
				'tant':self.tant,
				'mxtant':self.mxtant,
				'x':self.x,'y':self.y}

	def inport_data(self,data):
		self.lives=data['lives'] or 3
		self.score=data['score'] or 0
		self.tant=data['tant'] or 0
		self.mxtant=data['mxtant'] or 1
		self.x=data['x'] or 0
		self.y=data['y'] or 0


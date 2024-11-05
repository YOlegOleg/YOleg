
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
		self.lives=2

	def move(self,dx,dy):
		nx=self.x+dx
		ny=self.y+dy
		if nx>=0 and ny>=0 and nx<self.h and ny<self.w:
			self.x,self.y=nx,ny

	def print_stels (self):
		print('% ',self.tant,'/',self.mxtant,sep="",end='|')
		print('O:',self.score,end='|')
		print('L:',self.lives)
			
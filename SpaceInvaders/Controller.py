# Zach Ballard
# File: Controller.py
import viz
from modules import *

# Controller class inherits event handling methods from viz.EventClass
class Controller(viz.EventClass):
	def __init__(self):
		# must call constructor of EventClass first!!
		
		viz.EventClass.__init__(self)
		self.callback(viz.TIMER_EVENT,self.onTimer)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
		#spawning in the ship 
		self.ship = Ship()
		self.ship.setXY(self.ship.getX(), self.ship.getY() - 220)
		
		#bullet list to store and remove bullets 
		self.bulletList = []
		self.starttimer(1,1/25.0,viz.FOREVER)
		
		
		#list to store and remove aliens
		self.alienList1 = []
		self.xval = -150
		self.yval = 240
		
		#direction for moving aliens 
		self.direction = 0
		
		#spawning in the aliens 
		for cord in range(3):
			self.xval = -150
			self.yval = self.yval - 30
			for a in range(9):
				self.alien = Alien()
				self.alien.setXY(self.alien.getX() + self.xval, self.alien.getY() + self.yval)
				self.alienList1.append(self.alien)
				self.xval = self.xval + 40
	
	def onKeyDown(self,key):
		#moving left 
		if(key == viz.KEY_LEFT):
			self.ship.setXY(self.ship.getX() - 10, self.ship.getY())
		
		#moving right 
		if(key == viz.KEY_RIGHT):
			self.ship.setXY(self.ship.getX() + 10, self.ship.getY())
		
		#how it shoots the bullets
		if(key == " "):
			viz.playSound('shoot.wav')
			self.bullet = Bullet()
			self.bullet.setXY(self.ship.getX(), self.bullet.getY() - 190)
			self.bulletList.append(self.bullet)

	
	def onTimer(self,num):
		#moving alien left, right and down.
		for a in self.alienList1:
			#left 
			if self.direction == 0:
				if a.getX() != -310:
					a.setXY(a.getX() - 2, a.getY())
				else:
					self.direction = 1 
					for a in self.alienList1:
						a.setXY(a.getX(), a.getY() - 10)

			#right 
			if self.direction == 1:
				if a.getX() != 310:
					a.setXY(a.getX() + 2, a.getY())
				else:
					self.direction = 0
					for a in self.alienList1:
						a.setXY(a.getX(), a.getY() - 10)
				
		#shooting the bullets
		for b in self.bulletList:
			b.setXY(b.getX(), b.getY() + 10)
			
		#removing the aliens and bullets when hit
		for bu in self.bulletList:
			for al in self.alienList1:
				if (b.getX() < al.getX() + 10) and (b.getX() > al.getX() - 10) and (b.getY() < al.getY() + 7) and (b.getY() > al.getY() - 7):
					self.bulletList.remove(b)
					self.alienList1.remove(al)
					al.removeVert()
					b.removeVert()
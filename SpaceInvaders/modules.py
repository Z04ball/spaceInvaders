#Zach Ballard
#File: modules.py 
#02/11/2019
import viz
class Ship:
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y
		
		viz.startLayer(viz.QUADS)
		#main ship
		#bottom right
		viz.vertex(20, -8, 0)
		#bottom left
		viz.vertex(-20, -8, 0)
		#top left
		viz.vertex(-20, 10.5, 0)
		#top right
		viz.vertex(20, 10.5, 0)
		
		viz.startLayer(viz.QUADS)
		#left side
		#bottom right
		viz.vertex(-20, -8, 0)
		#bottom left
		viz.vertex(-22.5, -8, 0)
		#top left
		viz.vertex(-22.5, 7, 0)
		#top right
		viz.vertex(20, 7, 0)
		
		viz.startLayer(viz.QUADS)
		#right side
		#bottom right
		viz.vertex(20, -8, 0)
		#bottom left
		viz.vertex(22.5, -8, 0)
		#top left
		viz.vertex(22.5, 7, 0)
		#top right
		viz.vertex(20, 7, 0)
		viz.vertexColor(0, 1, 0)
		
		viz.startLayer(viz.QUADS)
		#cannon bottom
		#bottom right
		viz.vertex(4.5, 10.5, 0)
		#bottom left
		viz.vertex(-4.5, 10.5, 0)
		#top left
		viz.vertex(-4.5, 18.5, 0)
		#top right
		viz.vertex(4.5, 18.5, 0)
		
		viz.startLayer(viz.QUADS)
		#cannon top
		#top right
		viz.vertex(1.5, 21, 0)
		#top left
		viz.vertex(-1.5, 21, 0)
		#bottom left
		viz.vertex(-1.5, 18, 0)
		#bottom right
		viz.vertex(1.5, 18, 0)
		viz.vertexColor(0, 1, 0)
		
		self.quad = viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.quad.setMatrix(mat)
		
class Alien:
	def __init__(self,x = 0, y = 0, vx = 0, vy = 0):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0, 0, 0)
		#left eye
		#bottom left
		viz.vertex(-4.5, -1.8, 0)
		#bottom right
		viz.vertex(-3, -1.8, 0)
		#top right
		viz.vertex(-3, 2, 0)
		#top left
		viz.vertex(-4.5, 2, 0)
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(0, 0, 0)
		#right eye
		#bottom right
		viz.vertex(4.5, -1.8, 0)
		#bottom left
		viz.vertex(3, -1.8, 0)
		#top left
		viz.vertex(3, 2, 0)
		#top right
		viz.vertex(4.5, 2, 0)
		
		viz.startLayer(viz.QUADS)
		viz.vertexColor(1, 0.07, 0.57)
		#main body
		#bottom right
		viz.vertex(6, -5, 0)
		#bottom left
		viz.vertex(-6, -5, 0)
		#top left
		viz.vertex(-6, 4.2, 0)
		#top right
		viz.vertex(6, 4.2, 0)
		
		viz.startLayer(viz.QUADS)
		#left leg down 
		#top left
		viz.vertex(-6, -5, 0)
		#top right
		viz.vertex(-4.5, -5, 0)
		#bottom right
		viz.vertex(-4.5, -6.8, 0)
		#bottom left
		viz.vertex(-6, -6.8, 0)
		
		viz.startLayer(viz.QUADS)
		#left leg across
		#top left
		viz.vertex(-4.5, -6.8, 0)
		#top right
		viz.vertex(-2, -6.8, 0)
		#bottom right
		viz.vertex(-2, -8.6, 0)
		#bottom left
		viz.vertex(-4.5, -8.6, 0)
		
		viz.startLayer(viz.QUADS)
		#right leg down 
		#top right
		viz.vertex(6, -5, 0)
		#top left
		viz.vertex(4.5, -5, 0)
		#bottom left
		viz.vertex(4.5, -6.8, 0)
		#bottom right
		viz.vertex(6, -6.8, 0)
		
		viz.startLayer(viz.QUADS)
		#right leg across
		#top right
		viz.vertex(4.5, -6.8, 0)
		#top left
		viz.vertex(2, -6.8, 0)
		#bottom left
		viz.vertex(2, -8.6, 0)
		#bottom right
		viz.vertex(4.5, -8.6, 0)
		
		viz.startLayer(viz.QUADS)
		#right arm short
		#top left
		viz.vertex(6, 2.5, 0)
		#top right
		viz.vertex(7.5, 2.5, 0)
		#bottom right
		viz.vertex(7.5, -2.8, 0)
		#bottom left
		viz.vertex(6, -2.8, 0)
		
		viz.startLayer(viz.QUADS)
		#right arm long
		#bottom left
		viz.vertex(7.5, -6.8, 0)
		#top left
		viz.vertex(7.5, 1, 0)
		#top right
		viz.vertex(9, 1, 0)
		#bottom right
		viz.vertex(9, -6.8, 0)
		
		viz.startLayer(viz.QUADS)
		#left arm short
		#top right
		viz.vertex(-6, 2.5, 0)
		#top left
		viz.vertex(-7.5, 2.5, 0)
		#bottom left
		viz.vertex(-7.5, -2.8, 0)
		#bottom right
		viz.vertex(-6, -2.8, 0)
		
		viz.startLayer(viz.QUADS)
		#left arm long
		#bottom right
		viz.vertex(-7.5, -6.8, 0)
		#top right
		viz.vertex(-7.5, 1, 0)
		#top left
		viz.vertex(-9, 1, 0)
		#bottom left
		viz.vertex(-9, -6.8, 0)
		
		viz.startLayer(viz.QUADS)
		#bottom of left antenna(?), ear(?)
		#bottom left
		viz.vertex(-4.5, 4.2, 0)
		#bottom right
		viz.vertex(-3, 4.2, 0)
		#top right
		viz.vertex(-3, 5.7, 0)
		#top left
		viz.vertex(-4.5, 5.7, 0)
		
		viz.startLayer(viz.QUADS)
		#top of left antenna(?), ear(?)
		#bottom right
		viz.vertex(-4.5, 5.7, 0)
		#bottom left
		viz.vertex(-6, 5.7, 0)
		#top left
		viz.vertex(-6, 7.2, 0)
		#bottom right
		viz.vertex(-4.5, 7.2, 0)
		
		viz.startLayer(viz.QUADS)
		#bottom of right antenna(?), ear(?)
		#bottom right
		viz.vertex(4.5, 4.2, 0)
		#bottom left
		viz.vertex(3, 4.2, 0)
		#top left
		viz.vertex(3, 5.7, 0)
		#top right
		viz.vertex(4.5, 5.7, 0)
		
		viz.startLayer(viz.QUADS)
		#top of right antenna(?), ear(?)
		#bottom left
		viz.vertex(4.5, 5.7, 0)
		#bottom right
		viz.vertex(6, 5.7, 0)
		#top right
		viz.vertex(6, 7.2, 0)
		#bottom left
		viz.vertex(4.5, 7.2, 0)
		
		self.quad = viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def getVX(self):
		return self.vx
		
	def getVY(self):
		return self.vy
		
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.quad.setMatrix(mat)
		
	def setVXVY(self,vx,vy):
		self.vx = vx
		self.vy = vy
		
	def removeVert(self):
		self.quad.remove()
		
class Bullet:
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y

		
		viz.startLayer(viz.QUADS)
		#bullet
		viz.vertexColor(1, 1, 1)
		viz.vertex(.5, 0, 0)
		viz.vertex(-.5, 0, 0)
		viz.vertex(-.5, 2.9, 0)
		viz.vertex(.5, 2.9, 0)
		self.quad = viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	def setXY(self,x,y):
		self.x = x
		self.y = y
		mat = viz.Matrix()
		mat.postTrans(self.x, self.y)
		self.quad.setMatrix(mat)
		
	def removeVert(self):
		self.quad.remove()
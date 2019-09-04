# Zach Ballard
# File: runShapes.py
import viz 
from Controller import *

window = viz.MainWindow

window.ortho(-320, 320, -240, 240, -1, 1)
viz.window.setName( "Space Invaders" )

viz.eyeheight(0);

Controller()

vizact.onkeydown('b', viz.window.startRecording,'c:\\Temp\\spaceinvaders.avi')
vizact.onkeydown('e', viz.window.stopRecording)

viz.go()
        
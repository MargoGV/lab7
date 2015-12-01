import math
import pylab
from mathplotlib import mlab
F=[_F/100 for _F in range(-1000,1000,1) ]
pylab.ion()

for f in range (1000):
  x=[m.sin(_F+f/100) for _F in F]
  y=[m.cos(2*_F) for _F in F]
  pylab.clf()
  pylab.plot(x,y)
  pylab.draw()

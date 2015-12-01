import math
import mathplotlib.pyplot as plt

n=float(input())
m=float(input())
_x=[x/100 for x in range(-1000,1000)]
y=[sum([m**z*m.cos(n**z*m.pi*x) for z in range(100)]) for x in _x]

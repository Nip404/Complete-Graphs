# Complete Graphs
Visualising multiplication using complete graphs in Python 3.x using the Pygame library.
This code was inspired by [Mathologer's](https://www.youtube.com/channel/UC1_uAIS3r8Vu6JjXWvastJg) video on Youtube.\
You can find the video [here](https://www.youtube.com/watch?v=qhbuKbxJsk8).

You may find some interesting patterns at:

Factor = 103; Density = 8.5%\
Factor = 103; Density = 10.2%\
Factor = 154; Density = 48.45%\
Factor = 2; Density = 12%\
Factor = 31; Density = 4.5%\
Factor = 46; Density = 4.5%\
Factor = 501; Density = 12%\
Factor = 479; Density = 12%\
Factor = 929; Density = 12%\
Factor = 1041; Density = 12%\
Factor = 1041; Density = 12.35%\
Factor = 1041; Density = 15.8%\
Factor = 1053; Density = 3.9%\
Factor = 1063; Density = 36.4%\
Factor = 801; Density = 4%

# Maths
I calculate the coordinates of the circumference of the circle using these equations:
- x = cx + r * cos(theta)
- y = cy + r * sin(theta)

where (cx,cy) is the centre point of the circle, r is the radius, and theta is the angle in [radians](https://en.wikipedia.org/wiki/Radian).\
Note that radians=0 begins at the rightmost point on the circle.

Refer to this [wikipedia article](http://en.wikipedia.org/wiki/Circle#Equations) for more information on Parametric equations.

# Requirements
I am using the [Python 3.7](https://www.python.org/downloads/release/python-370/) IDLE.\
Python 3.6 and Pygame 1.7.x or above is required.\
You can download pygame either [here](https://www.pygame.org/download.shtml),[here](https://bitbucket.org/pygame/pygame/downloads/) or [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame).

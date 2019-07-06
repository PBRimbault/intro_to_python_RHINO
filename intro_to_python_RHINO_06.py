# Nested for loops
# Create our own function
# Colour points

import rhinoscriptsyntax as rs

def createColouredPoint(x,y,z,r,g,b):
    currentColour = (r,g,b)
    pt = rs.AddPoint(x,y,z)
    rs.ObjectColor(pt, currentColour)

rs.EnableRedraw(False)
step = 10

for x in range(0,256,step):
    for y in range(0,256,step):
        for z in range(0,256,step):
            createColouredPoint(x,y,z,x,y,z)

rs.Redraw()
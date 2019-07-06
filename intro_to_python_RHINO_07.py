# If Elif and Else statements

import rhinoscriptsyntax as rs
rs.EnableRedraw(False)

color01 = (255, 0, 255)     # magenta
color02 = (0, 255, 0)       # cyan
color03 = (125, 38, 205)    # purple

for x in range(0,100,1):
    for y in range(0,100,1):
        pt = rs.AddPoint(x,y,0)
        if x % 3 == 0 and y % 5 == 0:
            rs.ObjectColor(pt, color01)
        elif x % 3 == 0 or y % 5 == 0:
            rs.ObjectColor(pt, color02)
        else:
            rs.ObjectColor(pt, color03)


rs.Redraw()
from xml.dom import minidom
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
xmldoc = minidom.parse('plotMe.xml')
plt.axes()

lines = xmldoc.getElementsByTagName('Line')
arcs = xmldoc.getElementsByTagName('Arc')
for line in lines:
    xstart = line.getElementsByTagName('XStart')[0].firstChild.data
    
    xend = line.getElementsByTagName('XEnd')[0].firstChild.data
    ystart = line.getElementsByTagName('YStart')[0].firstChild.data
    yend = line.getElementsByTagName('YEnd')[0].firstChild.data
    try:
        color = line.getElementsByTagName('Color')[0].firstChild.data
    except IndexError:
        color = 'black'
    plt.plot([float(str(xstart)),float(str(xend))],[float(str(ystart)),float(str(yend))],color)
for arc in arcs:
    x = float(str(arc.getElementsByTagName('XCenter')[0].firstChild.data))
    y = float(str(arc.getElementsByTagName('YCenter')[0].firstChild.data))
    radius = 2*float(str(arc.getElementsByTagName('Radius')[0].firstChild.data))
    arcstart = float(str(arc.getElementsByTagName('ArcStart')[0].firstChild.data))
    arcend = float(str(arc.getElementsByTagName('ArcExtend')[0].firstChild.data))+arcstart
    try:
        colour = arc.getElementsByTagName('Color')[0].firstChild.data
    except IndexError:
        colour = 'black'
    arc = ptc.Arc((x,y),radius,radius,0,arcstart,arcend,color=colour)
    plt.gca().add_patch(arc)

plt.axis('scaled')
plt.show()



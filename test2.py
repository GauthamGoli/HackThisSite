import matplotlib.pyplot as plt
import matplotlib.patches as ptc
plt.axes()
arc = ptc.Arc((2,3),5,5,0,10,90,color='green')
plt.gca().add_patch(arc)
plt.axis('scaled')
plt.show()

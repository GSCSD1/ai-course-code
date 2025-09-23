"""
    fig.add_subplot(nros,nclos,plot_number)

"""

import matplotlib.pyplot as plt

fig = plt.figure()

ax1 =  fig.add_subplot(1,2,1)
ax1.plot([1,5],[6,12])

ax2 =  fig.add_subplot(1,2,2)
ax2.plot([3,5],[3,-2])

plt.show()
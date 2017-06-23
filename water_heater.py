import matplotlib.pyplot as plt
from numpy import genfromtxt

data=genfromtxt("water_heater.csv", delimiter=',',skip_header=0,skip_footer=0,names=['time','power1','power2','power3','power4'])
x=data['time']
#y=data['power']

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.plot(data['time'], data['power1'], color='k', label='total power')
"""
ax1 = fig.add_subplot(222)
ax1.plot(data['time'], data['power2'], color='b', label='total power')
ax1 = fig.add_subplot(223)
ax1.plot(data['time'], data['power3'], color='g', label='total power')
ax1 = fig.add_subplot(224)
ax1.plot(data['time'], data['power4'], color='r', label='total power')


ax1.set_title("Power consumption of devices")
ax1.set_xlabel('time in seconds')
ax1.set_ylabel("Power in watts")
ax1.grid(True)

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels)
"""


plt.show()


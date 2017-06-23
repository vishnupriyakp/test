import matplotlib.pyplot as plt
from numpy import genfromtxt

data=genfromtxt("fridge_2.csv", delimiter=',',skip_header=1,skip_footer=0,names=['time','power'])
x=data['time']
y=data['power']

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.plot(data['time'], data['power'], color='k', label='total power')
ax1.set_title("Power consumption of devices")
ax1.set_xlabel('time in seconds')
ax1.set_ylabel("Power in watts")
ax1.grid(True)

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels)


plt.show()


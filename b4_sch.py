import matplotlib.pyplot as plt
from numpy import genfromtxt

data=genfromtxt("41mins.csv", delimiter=',',skip_header=1,skip_footer=0,names=['time','boiler','fridge','freezer','mw','waterket','coffee','l1','l2','l3','l4', 'l5','total'])
x=data['time']
#y=data['power']

fig = plt.figure()

ax1 = fig.add_subplot(111)

'''ax1.plot(data['time'], data['boiler'], color='c', label='boiler')

ax1.plot(data['time'], data['fridge'], color='g', label='fridge') 

ax1.plot(data['time'], data['freezer'], color='r', label='freezer')

ax1.plot(data['time'], data['mw'], color='b', label='mw')

ax1.plot(data['time'], data['waterket'], color='g', label='kettle')

ax1.plot(data['time'], data['coffee'], color='y', label='coffee')'''



ax1.plot(data['time'], data['total'], color='k', label='total power')


ax1.set_title("Power consumption of devices")
ax1.set_xlabel('time in seconds')
ax1.set_ylabel("Power in watts")
ax1.grid(True)




handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels)


print data['time']
plt.show()



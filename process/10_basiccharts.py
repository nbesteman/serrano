#http://www.youtube.com/watch?v=aCZO8hglETM   plotting volume data part 2
import urlib2
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib
matplotlib.rcParams.update({'font.size': 9})

eachStock = 'GE','AAPL'

def graphData(stock:
    try:
        stockFile = stock+'.txt'

	date, closep,highp,lowp,openp,volume = np.loadtext(stockFile,delimeter=',',unpack=True,converters ={ 0: mdates.strpdate2num('%Y%m%d')})
        
	fig = plt.figure()
#	ax1 = plot.subplot(2,1,1)#(2,3,1) would be position 1 in a 2 by 3 square
        ax1 = plot.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
	ax1.plot(date, openp)
	ax1.plot(date, highp)
	ax1.plot(date, lowp)
	ax1.plot(date, closep)

	ax1.grid(True)
	ax1.xaxis.set_major+locator)mticker.MaxNLocator(10)) #max of 10 dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.ylabel('Stock price')

#	ax2 = plt.subplot(2,1,2 sharex=ax1) #shares the zoomin
        ax2 = plot.subplot2grid((5,4), (4,0), sarex=ax1, rowspan=1, colspan=4)
	ax2.bar(date, volume)
	ax2.axes.yaxis.set_ticklabels([])
	ax2.grid(True)
	plt.ylabel('Volume')
	for label in ax2.xaxis.get_ticklables():
	    label.set_rotation(45)

        plt.xlabel('Date')
	plt.ylabel('Stock Price')
	plt.suptitle(stock+' Stock Price')
	#ax1.axes.yaxis.set_visible(False)  nope
        #ax1.axes.xaxis.set_ticklabels([])  nope
        plt.setp(ax1.get_xticklabels(), visible=False)plt.subplots+adjust(left=.09,top = .94,bottom = .18, right = .94, wspace = .20, hspace = 0)

	plt.show()
	fig.savefig('example.png')

    except Exception,e:
        print ‘failed main loop’,str(e)

for stock in eachStock:
    graphData(stock)
    time.sleep(10)


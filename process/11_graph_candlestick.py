#http://www.youtube.com/watch?v=bCRtqX2LdlM   candelstick chart
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import matplotlib
matplotlib.rcParams.update({'font.size': 9})

eachStock = 'AAPL','MSFT','SLV','GLD'

def graphData(stock):
    try:
        stockFile = stock+'.txt'

        date, closep,highp,lowp,openp,volume = np.loadtxt(stockFile,delimiter=',',unpack=True,converters ={ 0: mdates.strpdate2num('%Y%m%d')})

        x = 0
	y = len(date)
	candleAr = []
	while x < y:
	    appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
	    candleAr.append(appendLine)
	    x+=1
#        

	fig = plt.figure()
#	ax1 = plot.subplot(2,1,1)#(2,3,1) would be position 1 in a 2 by 3 square
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
        candlestick(ax1, candleAr, width=.75, colorup ='g', colordown='r')

	ax1.grid(True)
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) #max of 10 dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.ylabel('Stock price')

#	ax2 = plt.subplot(2,1,2 sharex=ax1) #shares the zoomin
        ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=1, colspan=4)
	ax2.bar(date, volume)
	ax2.axes.yaxis.set_ticklabels([])
	ax2.grid(True)
	plt.ylabel('Volume')
	for label in ax2.xaxis.get_ticklabels():
	    label.set_rotation(45)

        plt.xlabel('Date')
	plt.ylabel('Stock Price')
	plt.suptitle(stock+' Stock Price')
	#ax1.axes.yaxis.set_visible(False)  nope
        #ax1.axes.xaxis.set_ticklabels([])  nope
        plt.setp(ax1.get_xticklabels(), visible=False)
	plt.subplots_adjust(left=.09,top = .94,bottom = .18, right = .94, wspace = .20, hspace = 0)

	plt.show()
        fig.savefig(stock+'.png')

    except Exception,e:
        print 'filed main loop',str(e)

for stock in eachStock:
    graphData(stock)
    time.sleep(1)


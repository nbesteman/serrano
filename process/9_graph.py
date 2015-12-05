#http://www.youtube.com/watch?v=zUArBZUGFaw   plotting volume data
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

eachStock = 'AAPL','MSFT','SLV','GLD'

def graphData(stock):
    try:
        stockFile = stock+'.txt'

	date, closep,highp,lowp,openp,volume = np.loadtxt(stockFile,delimiter=',',unpack=True,converters ={ 0: mdates.strpdate2num('%Y%m%d')})
        fig = plt.figure()
	ax1 = plt.subplot(2,1,1)#(2,3,1) would be position 1 in a 2 by 3 square
	ax1.plot(date, openp)
	ax1.plot(date, highp)
	ax1.plot(date, lowp)
	ax1.plot(date, closep)
	plt.ylabel('Stock price')
	ax1.grid(True)

	ax2 = plt.subplot(2,1,2, sharex=ax1) #shares the zoomin
	ax2.bar(date, volume)
	plt.ylabel('Volume')
	ax2.grid(True)
	
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) #max of 10 dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        for label in ax1.xaxis.get_ticklabels():
	    label.set_rotation(90)

	for label in ax1.xaxis.get_ticklabels():
	    label.set_rotation(45)

	plt.subplots_adjust(left=.10, bottom = .19, right = .93, wspace = .20, hspace = .07)
        plt.xlabel('Date')
	plt.suptitle(stock+' Stock Price')
	plt.show()

    except Exception,e:
        print 'failed main loop',str(e)

for stock in eachStock:
    graphData(stock)
    time.sleep(1)


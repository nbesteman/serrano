#7 http://www.youtube.com/watch?v=EyCxm1Sg-Eo
#6 is just the downloads
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
	#stockFile = ./build/stock+'.txt'

	date, closep,highp,lowp,openp,volume = np.loadtxt(stockFile,delimiter=',',unpack=True,converters ={ 0: mdates.strpdate2num('%Y%m%d')})
        fig = plt.figure()
	ax1 = plt.subplot(1,1,1)#(2,3,1) would be position 1 in a 2 by 3 square
	ax1.plot(date, openp)
	ax1.plot(date, highp)
	ax1.plot(date, lowp)
	ax1.plot(date, closep)
	
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) #max of 10 dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	for label in ax1.xaxis.get_ticklabels():
	    label.set_rotation(45)

	plt.show()
    except Exception,e:
        print 'failed main loop',str(e)

for stock in eachStock:
    graphData(stock)
    time.sleep(1)


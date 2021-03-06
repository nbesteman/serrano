#https://www.youtube.com/watch?v=yXatuqBimbo
#fixing Volume problem and colors of SMA over candlestick charts

import urllib2
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

#area of focus for Simple Moveing Average
def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def graphData(stock,MA1,MA2):
    try:
        stockFile = stock+'.txt'

        date, closep,highp,lowp,openp,volume = np.loadtxt(stockFile,delimiter=',',unpack=True,converters ={ 0: mdates.strpdate2num('%Y%m%d')})

        ###
        x = 0
	y = len(date)
	candleAr = []
	while x < y:
	    appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
	    candleAr.append(appendLine)
	    x+=1
#        
        Av1 = movingaverage(closep, MA1)
	Av2 = movingaverage(closep, MA2)

	SP = len(date[MA2-1:])  #starting point is array of MA2 exact number

        label1 = str(MA1)+' SMA'
	label2 = str(MA1)+' SMA'

	fig = plt.figure(facecolor='#07000d')  #change facecolor (frame) to black
#	ax1 = plot.subplot(2,1,1)#(2,3,1) would be position 1 in a 2 by 3 square
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4, axisbg='#07000d')
# this will extend the candlestick left of the Moving averages....	candlestick(ax1, candleAr, width=1, colorup ='#9eff15', colordown='#ff1717',shadowCol='w'
	candlestick(ax1, candleAr[-SP:], width=1, colorup ='#9eff15', colordown='#ff1717',shadowCol='w')



#color of volume
        ax1.plot(date[-SP:],Av1[-SP:],'#5998ff',label=label1, linewidth=1.5)
	ax1.plot(date[-SP:],Av2[-SP:],'#e1edf9',label=label2, linewidth=1.5)

	ax1.grid(True, color = 'w')
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) #max of 10 dates
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	ax1.yaxis.label.set_color('w')
	ax1.spines['bottom'].set_color('#5998ff')
	ax1.spines['top'].set_color('#5998ff')
	ax1.spines['left'].set_color('#5998ff')
	ax1.spines['right'].set_color('#5998ff')
	ax1.tick_params(axis='y',colors='w')
	plt.ylabel('Stock price')
	plt.legend(loc=3,prop={'size':7}, fancybox=True)

        #volumeMin = volume.min()
	volumeMin = 0

#	ax2 = plt.subplot(2,1,2 sharex=ax1) #shares the zoomin
        ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
#       ax2.bar(date, volume)
	ax2.plot(date, volume, '#00ffe8', linewidth = .8)
        ax2.fill_between(date,volumeMin, volume, facecolor='#00ffe8', alpha = .4)
	ax2.axes.yaxis.set_ticklabels([])
	ax2.grid(False)
	ax2.spines['bottom'].set_color('#5998ff')
	ax2.spines['top'].set_color('#5998ff')
	ax2.spines['left'].set_color('#5998ff')
	ax2.spines['right'].set_color('#5998ff')
	ax2.tick_params(axis='x',colors='w')
	ax2.tick_params(axis='y',colors='w')

	plt.ylabel('Volume', color = 'w')
	for label in ax2.xaxis.get_ticklabels():
	    label.set_rotation(45)

 #       plt.xlabel('Date',color = 'w')
	plt.ylabel('Volume')
	plt.suptitle(stock+' Stock Prisce',color ='w')
	#ax1.axes.yaxis.set_visible(False)  nope
        #ax1.axes.xaxis.set_ticklabels([])  nope
        plt.setp(ax1.get_xticklabels(), visible=False)
	plt.subplots_adjust(left=.09,top = .95,bottom = .14, right = .94, wspace = .20, hspace = 0)

	plt.show()
        fig.savefig(stock+'.png',facecolor=fig.get_facecolor())

    except Exception,e:
        print 'filed main loop',str(e)

for stock in eachStock:
    graphData(stock,12,26)
    #graphData(stock,50,20)
    time.sleep(1)


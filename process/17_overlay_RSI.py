#https://www.youtube.com/watch?v=SYvjaL2pWZw
#adding relative Strength Indicator

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

	fig = plt.figure(facecolor='#07000d')

	ax0= plt.subplot2grid((5,4), (0,0), rowspan=1, colspan=4, axisbg='#07000d')
	ax0.spines['bottom'].set_color('#5998ff')
	ax0.spines['top'].set_color('#5998ff')
	ax0.spines['left'].set_color('#5998ff')
	ax0.spines['right'].set_color('#5998ff')
	ax0.tick_params(axis='x',colors='w')
	ax0.tick_params(axis='y',colors='w')
	ax0.yaxis.label.set_color('w')
	plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='lower'))
	plt.ylabel('RSI')

        ax1 = plt.subplot2grid((5,4), (1,0), rowspan=4, colspan=4, axisbg='#07000d')
	candlestick(ax1, candleAr[-SP:], width=1, colorup ='#9eff15', colordown='#ff1717')

        label1 = str(MA1)+' SMA'
	label2 = str(MA1)+' SMA'
	#fig = plt.figure(facecolor='#07000d')  #change facecolor (frame) to black

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
	ax1.tick_params(axis='x',colors='w')
	plt.ylabel('Stock price')

	for label in ax1.xaxis.get_ticklabels():
	    label.set_rotation(45)

	plt.legend(loc=3,prop={'size':7}, fancybox=True, borderaxespad=0.)

	volumeMin = 0

#ax 1 volume - this is to set up the volume overlay for the Relative Strength Index
        ax1v = ax1.twinx() #shares the axis.
	ax1v.fill_between(date,volumeMin, volume, facecolor='#00ffe8', alpha = .4)
	ax1v.axes.yaxis.set_ticklabels([])
	ax1v.grid(False)
	ax1v.spines['bottom'].set_color('#5998ff')
	ax1v.spines['top'].set_color('#5998ff')
	ax1v.spines['left'].set_color('#5998ff')
	ax1v.spines['right'].set_color('#5998ff')
	ax1v.set_ylim(0, 5*volume.max())  #changes the size of the volume chart
	ax1v.tick_params(axis='x',colors='w')
	ax1v.tick_params(axis='y',colors='w')

	plt.suptitle(stock,color ='w')

        plt.setp(ax0.get_xticklabels(), visible=False)
	plt.subplots_adjust(left=.09,top = .95,bottom = .14, right = .94, wspace = .20, hspace = 0)

	plt.show()
        fig.savefig(stock+'.png',facecolor=fig.get_facecolor())

    except Exception,e:
        print 'main loop',str(e)

for stock in eachStock:
    graphData(stock,12,26)
    #graphData(stock,50,20)
    time.sleep(1)


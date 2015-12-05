#https://www.youtube.com/watch?v=sFv-gp4BZNU
#how to calc exponential moving average
#macd is moving aveerage convergence divergence
# which is a trend following and momentum indicator
#the macd has 3 different lines to it
# it has the macd line is the 12 period exponential moving average / 26 period exponential moving average
# the signal line 9 day exponential moving average / macd line
#macd histogram which is the macdline - the signal line
# the exponential moving average places more emphasis on more recent data
#so we need a function for an exponential moving average and then the macd function

import urllib2
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
#from matplotlib.finance import candlestick_ochl
import matplotlib
import pylab
matplotlib.rcParams.update({'font.size': 9})
path = '/home/nbesteman/apps/python/mycharts/tutorial/'
eachStock = 'MXL','TSS'
#14 is the default period (is this last 14 days?)
#100/1-relative strength
def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)
    for i in range(n, len(prices)):
	delta = deltas[i-1]
	if delta > 0:
	    upval = delta
	    downval = 0.
	else:
		upval = 0.
		downval = -delta
	up = (up*(n-1)+upval)/n
	down = (down*(n-1)+downval)/n
	rs = up/down
	rsi[i] = 100. - 100./(1.+rs)
    return rsi

#area of focus for Simple Moveing Average
def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas # as a numpy array

def ExpMovingAverage(values,window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()   # /= works like +=
    a = np.convolve(values, weights, mode ='full')[:len(values)]
    a[:window] = a[window]
    return a

def computeMACD(x, slow=26, fast=12):
    '''
    macd line = 12ema - 26ema
    signal line = 9ema of the macd line
    histogram = macd line - signal line
    '''
    emaslow = ExpMovingAverage(x, slow)
    emafast = ExpMovingAverage(x, fast)
    return emaslow, emafast, emafast-emaslow

def graphData(stock,MA1,MA2):
    try:
	stockFile = path+stock+'.txt'
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

        ax1 = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4, axisbg='#07000d') #the subplotgrid((6,4 sets the size of the grid
	#candlestick_ochl(ax1, candleAr[-SP:], width=1, colorup ='#9eff15', colordown='#ff1717')
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
	plt.ylabel('Stock Price and Volume')

	maLeg = plt.legend(loc=9,ncol=2, prop={'size':7}, fancybox=True, borderaxespad=0.)
	maLeg.get_frame().set_alpha(0.4)
	textEd = pylab.gca().get_legend().get_texts()
	pylab.setp(textEd[0:5], color = 'w')

	ax0= plt.subplot2grid((6,4), (0,0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
        rsi = rsiFunc(closep)
        rsiCol = '#00ffe8'
	ax0.plot(date[-SP:],rsi[-SP:],rsiCol,linewidth=1.5)
        ax0.axhline(70, color = rsiCol)
	ax0.axhline(30, color = rsiCol)
	ax0.fill_between(date[-SP:],rsi[-SP:], 70, where=(rsi[-SP:]>=70), facecolor =rsiCol, edgecolor = rsiCol)
	ax0.fill_between(date[-SP:],rsi[-SP:], 30, where=(rsi[-SP:]<=30), facecolor =rsiCol, edgecolor = rsiCol)
	ax0.spines['bottom'].set_color('#5998ff')
	ax0.spines['top'].set_color('#5998ff')
	ax0.spines['left'].set_color('#5998ff')
	ax0.spines['right'].set_color('#5998ff')
	ax0.tick_params(axis='x',colors='w')
	ax0.tick_params(axis='y',colors='w')
	ax0.set_yticks([30,70])
	ax0.yaxis.label.set_color('w')
#	plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='lower'))
	plt.ylabel('RSI')

	volumeMin = 0

#ax 1 volume - this is to set up the volume overlay for the Relative Strength Index
        ax1v = ax1.twinx() #shares the axis.
#	ax1v.fill_between(date,volumeMin, volume, facecolor='#00ffe8', alpha = .4)
	ax1v.fill_between(date[-SP:],volumeMin, volume[-SP:], facecolor='#00ffe8', alpha = .4)
	ax1v.axes.yaxis.set_ticklabels([])
	ax1v.grid(False)
	ax1v.spines['bottom'].set_color('#5998ff')
	ax1v.spines['top'].set_color('#5998ff')
	ax1v.spines['left'].set_color('#5998ff')
	ax1v.spines['right'].set_color('#5998ff')
	ax1v.set_ylim(0, 5*volume.max())  #changes the size of the volume chart
	ax1v.tick_params(axis='x',colors='w')
	ax1v.tick_params(axis='y',colors='w')

        ax2 = plt.subplot2grid((6,4), (5,0), sharex=ax1, rowspan=1,colspan=4, axisbg='#07000d')
	fillcolor='#00ffe8'
        nslow = 26
	nfast = 12
	nema = 9

	emaslow,emafast, macd = computeMACD(closep)
	ema9 = ExpMovingAverage(macd, nema)

	ax2.plot(date[-SP:],macd[-SP:])
	ax2.plot(date[-SP:],ema9[-SP:])
	ax2.fill_between(date[-SP:], macd[-SP:]-ema9[-SP:], alpha=0.5, facecolor=fillcolor, edgecolor=fillcolor)

	ax2.spines['bottom'].set_color('#5998ff')
	ax2.spines['top'].set_color('#5998ff')
	ax2.spines['left'].set_color('#5998ff')
	ax2.spines['right'].set_color('#5998ff')
	ax2.tick_params(axis='x',colors='w')
	ax2.tick_params(axis='y',colors='w')
	plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
        plt.ylabel('MACD',color = 'w')
	for label in ax2.xaxis.get_ticklabels():
	    label.set_rotation(45)

	plt.suptitle(stock,color ='w')

        plt.setp(ax0.get_xticklabels(), visible=False)
        plt.setp(ax1.get_xticklabels(), visible=False)

	plt.subplots_adjust(left=.09,top = .95,bottom = .14, right = .94, wspace = .20, hspace = 0)

	plt.show()
        fig.savefig(path+stock+'.png',facecolor=fig.get_facecolor())

    except Exception,e:
        print 'main loop',str(e)

for stock in eachStock:
    graphData(stock,20,200)
    #graphData(stock,50,20)
    time.sleep(1)

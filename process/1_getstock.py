#datetime is unix and in seconds
import urllib2
import time
import datetime

stocksToPull = 'AAPL','GOOG'

def pullData(stock):
    try:
        print 'pulling ',stock
	print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y=%m-%d %H:%M:%S'))
        utlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'\/chartdata;type=quote;range=1yr/csv'
        saveFileLine = stock+'.txt'
        #if timestamp is greater than the last time then save the data
	#IfEL would be better
	try:
	    readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.split('\n')
	    mostRecentLine = splitExisting[-2]
	    lastUnix = int(mostRecentLine.split(',')[0])
	except:
	    lastUnix = 0
    except Exception,e:
        print 'main loop',str(e)

    for eachStock in stocksToPull:
        pullData(stocksToPull)


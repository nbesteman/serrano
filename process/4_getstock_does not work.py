#getstocks number 4
#http://www.youtube.com/watch?v=rmGXek7qtVM
#5 minute high low data
#delete stock files
#did not run this one
import urllib2
import time
import datetime
path = '/home/nbesteman/apps/python/mycharts/tutorial/'
stocksToPull = 'AAPL','MSFT'
def pullData(stock):
    try:
        print 'pulling ',stock
	print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y=%m-%d %H:%M:%S'))
        #urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
	urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
	#http://chartapi.finance.yahoo.com/instrument/1.0/MSFT/chartdata;type=quote;range=10d/csv
	#http://chartapi.finance.yahoo.com/instrument/1.0/MSFT/chartdata;type=quote;range=1y/csv
        saveFileLine = path+stock+'.txt'
        #if timestamp is greater than the last time then save the data
	#If else would be better
	try:
	    readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.split('\n')
	    mostRecentLine = splitExisting[-2]
	    lastUnix = int(mostRecentLine.split(',')[0])
	except:
	    lastUnix = 0

#below this was not in the video
    except Exception,e:
        print 'main loop',str(e)

    for eachStock in stocksToPull:
        pullData(eachStock)


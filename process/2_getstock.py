#1 gives and intro, where to download python and how the yahho data datetime is unix and in seconds
#2 he uses idle  
import urllib2
import time
import datetime

stocksToPull = 'AAPL'

def pullData(stock):
    try:
        fileLine = stock+'.txt'
	urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

	for eachLine in splitSource:
	    splitLine = eachLine.split(',')
            if len(splitLine)==6:
                if 'volume' not in eachLine:
		    saveFile = open(fileLine,'a')
		    lineToWrite = eachLine+'\n'
                    saveFile.write(lineToWrite)
	print 'pulled',stock
	print 'sleeping'
	time.sleep(5)

    except Exception,e:
        print 'main loop',str(e)

#    for eachStock in stocksToPull:
#        pullData(stockToPull)

pullData(stocksToPull)

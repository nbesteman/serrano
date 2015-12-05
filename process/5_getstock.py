#http://www.youtube.com/watch?v=OXaxZpgBMqc
#part 5 finishes 4
import urllib2
import time
import datetime
i = 0
#stocksToPull = 'AAPL','MSFT','SLV','GLD'
stocksToPull = 'UNG','USO','SLV','GOV'

def pullData(stock):
    try:
        print 'pulling ',stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        #urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        saveFileLine = stock+'.txt'
        try:
	    readExistingData = open(saveFileLine,'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
	    lastUnix = int(mostRecentLine.split(',')[0])
    	except Exception,e:
	    print str(e)
	    time.sleep(1)
	    lastUnix = 0

        saveFile = open(saveFileLine,'a')
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            if 'values' not in eachLine:
	            splitLine = eachLine.split(',')
	            if len(splitLine)==6:
	                if int(splitLine[0]) > int(lastUnix):  
	                #if splitLine[0] > lastUnix: 
		            lineToWrite = eachLine+'\n'
			    saveFile.write(lineToWrite)
    	saveFile.close()
        print 'Pulled',stock
	print 'sleeping...'
	print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(2)

    except Exception,e:
        print 'main loop',str(e)

#while i < 2:
for eachStock in stocksToPull:
    pullData(eachStock)
    time.sleep(2) #can do this for a 1800 second wait
    i+=1



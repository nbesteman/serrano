#getstocks number 3
#add multiple stocks and use a for loop
#http://www.youtube.com/watch?v=UeyP_tELq6E
#delete the stocks
import urllib2
import time
import datetime
path = '/home/nbesteman/apps/python/mycharts/process/'
stocksToPull = 'MXL','UBOH','TSS','GLD','SLV','AAPL','MSFT','USO','UNG'
#open high low close ???
def pullData(stock):
    try:
        fileLine = path+stock+'.txt'
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
	time.sleep(2)

    except Exception,e:
        print 'main loop' ,str(e)

for eachStock in stocksToPull:
    pullData(eachStock)

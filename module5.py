import urllib
import urllib2

urlToRequest = "https://raw.githubusercontent.com/scotasaurus/Mouse-Squad-Module-5/master/sample.html"

request = urllib2.Request(urlToRequest)
response = urllib2.urlopen(request)

data = response.read()
print data

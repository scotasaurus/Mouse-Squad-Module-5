import urllib
import urllib2

urlToRequest = "http://www.google.com/"

request = urllib2.Request(urlToRequest)
response = urllib2.urlopen(request)

data = response.read()
print data

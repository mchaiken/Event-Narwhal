import urllib2, json

def getSong(tag):
#need to note for multiple tags
    url="http://8tracks.com/mix_sets/tags:"+tag.lower()+".json?api_key=52947991b38f982d9dc6842c0bd653fcd0df0a20&include=mixes"
    #print url
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    return url

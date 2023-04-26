import urllib.request
import json

def get_result(teamId,api_uri,gamedate):
    uri = "%s?team=%s&sarcasm=%s&date=%s"%(api_uri,teamId,'false',gamedate)
    response = urllib.request.urlopen(uri)
    data = response.read().decode('utf-8')
    print (data)
    return data

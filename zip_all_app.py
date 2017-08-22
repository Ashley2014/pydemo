import os
import zipfile
from time import gmtime, strftime
import urllib
import urllib2
import json
import pickle
values = {}
values['p1'] = "a"
values['p2'] = "b"
data = urllib.urlencode(values)
url = "http://localhost:8000"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
resStr=response.read()

print resStr
myList=json.loads(resStr)
# print myList

# myList = [s.encode('utf-8') for s in myList]

for item in myList:
    itemJson=json.dumps(item).decode('unicode_escape')
    itemDict = item
    print itemDict['id']
    print itemDict['name']
    # print json.dumps(item).decode('utf-8')
# print response.read()



def zipdir(path, ziph,id):
    # ziph is zipfile handle

    for root, dirs, files in os.walk(path):
        for file in files:
            print(root, dirs, files)
            if file=='app.js' and root=='dist/':
                with open(root+file, 'r') as myfile:
                    data = myfile.read().replace('REQUEST_MERCHANT_VALUE', str(id))
                    print(data)
                    ziph.writestr(os.path.join(str(id)+root, file), data)
            else:
                ziph.write(os.path.join(root, file),os.path.join(str(id)+root, file))





if __name__ == '__main__':
    time=strftime("%Y-%m-%d-%H:%M:%S", gmtime())

    if not os.path.exists('dists'):
      os.makedirs('dists')

    zipf = zipfile.ZipFile('dists/thuu'+ '.zip', 'w', zipfile.ZIP_DEFLATED)

    for i in range(1, 3):
        zipdir('dist/', zipf,i)


    zipf.close()

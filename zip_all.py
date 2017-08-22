import os
import zipfile

import urllib
import urllib2

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()



def zipdir(path, ziph,id):
    # ziph is zipfile handle

    for root, dirs, files in os.walk(path):
        for file in files:
            print(root, dirs, files)
            if file=='app.js':
                with open(root+file, 'r') as myfile:
                    data = myfile.read().replace('REQUEST_MERCHANT_VALUE', str(id))
                    print(data)
                    ziph.writestr(os.path.join(str(id)+root, file), data)
            else:
                ziph.write(os.path.join(root, file),os.path.join(str(id)+root, file))




if __name__ == '__main__':

    zipf = zipfile.ZipFile('test' + '.zip', 'w', zipfile.ZIP_DEFLATED)
    for i in range(1, 3):
        zipdir('dist/', zipf,i)
    zipf.close()
import os
import zipfile

def zipdir(path, ziph,id):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            print(root, dirs, files)
            if file=='app.js':
                with open(root+file, 'r') as myfile:
                    data = myfile.read().replace('REQUEST_MERCHANT_VALUE', str(id))
                    print(data)
                    ziph.writestr(os.path.join(root, file), data)
            else:
                ziph.write(os.path.join(root, file))


if __name__ == '__main__':



    for i in range(1, 3):
        zipf = zipfile.ZipFile('test'+str(i)+'.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir('dist/', zipf,i)
        zipf.close()
import time
import picamera
import datetime
import urllib2
import os
import requests
from PIL import Image


def internet_on():
    try:
        response=urllib2.urlopen('http://www.bing.com', timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

url = 'http://SERVER/camera.php'

#check if WIFI avaiable
if internet_on():
    #Wifi is on
    #collect filenames in the certain dictionary
    pics = []
    for root, dirs, files in os.walk('/home/pi/pic/'):
        for file in files:
    	    if file.endswith('.jpg'):
		path = os.path.join(root, file)
		filesize = os.stat(path).st_size
    		if filesize > 0:
		    pics.append(file)
		else:
		    os.remove(path)

    print(pics)

    #determeine the remote identify to updload

    for filename in pics:
	current_name = '/home/pi/pic/' +filename
	current_file = {'userfile': open(current_name, 'rb')}

	#process image
	im = Image.open(current_name)
	out = im.rotate(180)
	out.save(current_name)

	r = requests.post(url, files=current_file)	
	print('Uploading...' + str(filename) + ' -> ' + str(r.text)  )

	#save a thumbnail
	out = im.resize((128, 77))
	out.save('/home/pi/thumbnail/' +filename)

        #move uploaded file to another dictionary
	
	os.rename(current_name, '/home/pi/uploaded/' +filename)

	#relase uploaded file if storge goes short

        print('Uploaded!')



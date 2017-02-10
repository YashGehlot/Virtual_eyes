# Creatng a web server using python bottle Framework to create a local server
# to be able to run our model on our local machine
# which may then be actually shifted on to a Windows Azure Server 

import base64
import os
from bottle import route, run, template,response, get, post,request, static_file

# convert the base64 image string into a jpg image, so that we may run our 
# Image Classifier

def get_image1(imagedata, name):
	print "get_image"
	fh = open("../darknet/inputImage.jpg", "wb")
	fh.write(imagedata.decode('base64'))
	fh.close()
	runYolo()            # runs the Image classifier over the jpg image

# runs our Image Processing classifier
def runYolo():
	import subprocess
	print "start"
	os.system('sh runyolo.sh')	
	print "end"

# encodes the jpg image with our detections back into a base64 string and
# sends it back to our device 
def sendImage():
	print "sendImage"
	with open("../darknet/predictions.jpg", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
		#print encoded_string
    	return encoded_string
    
#here in we obtain the image that we sent over to our server
#via post method and obtain the image as a base64 string

@post('/getimage')
def login_page():	
	print "getimage"
	image = request.forms.get('image')
	name = request.forms.get('name')
	# print image,name
	get_image1(image,name)
	# import time
	# time.sleep(10)
	encodedimage = sendImage()
	print encodedimage
	return encodedimage



# run the server with a particular ip address
run(host='192.168.208.81', port=8080, debug=True)  


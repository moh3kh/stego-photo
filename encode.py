#!/bin/python
#This program uses LSB of RGB pictures to hide  secret message inside a picture
#By Mohamed Khalil

import Image
import stepic
import argparse
import hashlib
import sys
import getpass

def Main():

	parser = argparse.ArgumentParser()	
	
	parser.add_argument("-i", "--input", help="specify image to have secret message",required=True)
	parser.add_argument("-o", "--output", help="specify output image including secret message",required=True)
	parser.add_argument("-t", "--text", help="specify text to hide",type=str, required=True)
	parser.add_argument('-p','--password', help="enter password to lock",required=True)
	
	args = parser.parse_args()
		
##Password to lock		
	if args.text:
		username=getpass.getuser()
		f = open("/home/"+username+"/Documents/hashed.txt", "w")
		data = hashlib.md5(args.password).hexdigest()
		f.write(data)
		f.close()
		
		im=Image.open(args.input)
		im2=stepic.encode(im, args.text)
		im2.save(args.output)
		im2=Image.open(args.output)
		#im2.show()
		#im.show()

	
if __name__ == '__main__':
	Main()





#!/bin/python
#This code to extract the secret message from the encoded image

import Image
import stepic
import hashlib
import sys
import argparse
import getpass

def Main():
	username=getpass.getuser()	
	f = open("/home/"+username+"/Documents/hashed.txt", "ro")
	data = f.read()
	f.close()

	parser = argparse.ArgumentParser()	
	parser.add_argument('-p','--password', help="enter password to get the secret message",required=True)
	parser.add_argument("-i", "--input", help="specify image to have secret message",required=True)
	
	args = parser.parse_args()
	
	if args.password:
	
		if hashlib.md5(args.password).hexdigest() == data:
			im1=Image.open(args.input)
			s=stepic.decode(im1)
			data=s.decode()
			print data

		else:
			print "Wrong Password"
	else:
		print parser.usage

if __name__ == '__main__':
	Main()

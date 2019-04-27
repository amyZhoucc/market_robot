# -- coding: utf-8 --
#import RPi.GPIO as GPIO
import serial			#打开串口通信
import time
def init():
	t = serial.Serial("/dev/ttyUSB0",9600)
	temp = '0'
	t.write(temp.encode())

#货物拍照，参数为1,2,3,4
def good_arm(name):			
	t = serial.Serial("/dev/ttyUSB0",9600)
	if name == 1:
		temp = '3'
		t.write(temp.encode())
	elif name == 2:
		temp = '4'
		t.write(temp.encode())
	elif name == 3:
		temp = '1'
		t.write(temp.encode())
	elif name == 4:
		temp = '2'
		t.write(temp.encode()) 

#货仓拍照，参数为'a','b','c','d'
def ware_arm(name):		
	t = serial.Serial("/dev/ttyUSB0",9600)
	if name == 'a':
		temp = '1'
		t.write(temp.encode())
	elif name == 'b':
		temp = '2'
		t.write(temp.encode())
	elif name == 'c':
		temp = '3'
		t.write(temp.encode())
	elif name == 'd':
		temp = '4'
		t.write(temp.encode())

#做好准备抓取动作
def gesture():				
	t = serial.Serial("/dev/ttyUSB0",9600)
	temp = 'm'
	t.write(temp.encode())
	while True:
		x = ""
		flag = True
		# print(type(x))
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			# print(str_in)
			# print(type(str_in))
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			# print(x)
			# print(x == 'ok')
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				# print("in")
				break;
		time.sleep(0.1)
	return "o"

#货物抓取，根据不同的货物使用不同的力度
def grab_good(name):			
	t = serial.Serial("/dev/ttyUSB0",9600)
	t.write(name.encode())
	while True:
		x = ""
		flag = True
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			# print(str_in)
			# print(type(str_in))
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)
	return "o"


#货仓上下层准备
def place_ware(name):			
	t = serial.Serial("/dev/ttyUSB0",9600)
	t.write(name.encode())
	while True:
		x = ""
		flag = True
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			# print(str_in)
			# print(type(str_in))
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)
	return "o"

#货物放置
def place(name):			
	t = serial.Serial("/dev/ttyUSB0",9600)
	t.write(name.encode())
	while True:
		x = ""
		flag = True
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			# print(str_in)
			# print(type(str_in))
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)
	return "o"

#退回去回复原来动作
def retrive(name):
	t = serial.Serial("/dev/ttyUSB0",9600)
	t.write(name.encode())
	while True:
		x = ""
		flag = True
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			# print(str_in)
			# print(type(str_in))
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			# print("in if")
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)
	return "o"
	
if __name__ == '__main__':
	# good_arm(1)
	init()
	time.sleep(1)
	good_arm(3)
	time.sleep(1)
	gesture()

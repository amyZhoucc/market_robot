# -- coding: utf-8 --
#import RPi.GPIO as GPIO
import serial			#打开串口通信
import time

def init():				#传输给控制器2
	t = serial.Serial("/dev/ttyUSB1",9600)
	temp = "a010b020c040"	
	t.write(temp.encode())
	# while True:			#传回完成信息
	# 	x = ""
	# 	flag = True
	# 	while t.inWaiting() > 0:
	# 		str_in = t.read(t.inWaiting())
	# 		x += str(str_in)
	# 		time.sleep(0.01)
	# 		flag = False
	# 	if flag == False:
	# 		x = x.split('\'')[1]
	# 		print("res"+str(x))
	# 		if x == "o":
	# 			break;
	# 	time.sleep(0.1)

#货物拍照，参数为1,2,3,4
def good_arm(name):		#传输给控制器1			
	t = serial.Serial("/dev/ttyUSB0",9600)
	if name == 1:
		temp = '4'
		print("send")
		t.write(temp.encode())
	elif name == 2:
		temp = '1'
		print("send")
		t.write(temp.encode())
	elif name == 3:
		temp = '2'
		print("send")
		t.write(temp.encode())
	elif name == 4:
		temp = '3'
		print("send")
		t.write(temp.encode()) 

#货仓拍照，参数为'a','b','c','d'
def ware_arm(name):		#传输给控制器1	
	t = serial.Serial("/dev/ttyUSB0",9600)
	if name == 'a':
		temp = '2'
		t.write(temp.encode())
	elif name == 'b':
		temp = '3'
		t.write(temp.encode())
	elif name == 'c':
		temp = '4'
		t.write(temp.encode())
	elif name == 'd':
		temp = '1'
		t.write(temp.encode())

#做好准备抓取动作
def gesture():			#传输给控制器2			
	t = serial.Serial("/dev/ttyUSB1",9600)
	temp = "a010b060c170"	
	t.write(temp.encode())
	while True:
		x = ""
		flag = True
		# print(type(x))
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				# print("in")
				break;
		time.sleep(0.1)

#爪子动作：张开和闭合
def paw(name):				#传输给控制器1
	t = serial.Serial("/dev/ttyUSB0",9600)
	t.write(name.encode())
	while t.inWaiting() > 0:
		str_in = t.read(t.inWaiting())
		x += str(str_in)
		time.sleep(0.01)
		flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)		

#位置向下
def gooddown():			#传输给控制器2
	t = serial.Serial("/dev/ttyUSB1",9600)
	temp = "a015b060c180"	
	t.write(temp.encode())
	while True:
		x = ""
		flag = True
		# print(type(x))
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)

#货物抓取，根据不同的货物使用不同的力度
def grab_good(name):	#传输给控制器1		
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

#货仓上下层准备
def place_ware(name):	#传输给控制器2			
	t = serial.Serial("/dev/ttyUSB1",9600)
	if name == 'h':
		temp = "a095b080c100"	
	elif name == 'j':
		temp = "a010b050c160"
	t.write(temp.encode())
	while True:
		x = ""
		flag = True
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)

#向下放置
def waredown(name):			#传输给控制器2
	t = serial.Serial("/dev/ttyUSB1",9600)
	if name == 'h':
		temp = "a095b080c115"	
	elif name == 'j':
		temp = "a005b035c170"	
	t.write(temp.encode())
	while True:
		x = ""
		flag = True
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			x += str(str_in)
			time.sleep(0.01)
			flag = False
		if flag == False:
			x = x.split('\'')[1]
			print("res"+str(x))
			if x == "o":
				break;
		time.sleep(0.1)

#货物放置
# def place():		#传输给控制器1			
# 	t = serial.Serial("/dev/ttyUSB0",9600)
# 	temp = 's'
# 	t.write(temp.encode())
# 	while True:
# 		x = ""
# 		flag = True
# 		while t.inWaiting() > 0:
# 			str_in = t.read(t.inWaiting())
# 			x += str(str_in)
# 			time.sleep(0.01)
# 			flag = False
# 		if flag == False:
# 			x = x.split('\'')[1]
# 			print("res"+str(x))
# 			if x == "o":
# 				break;
# 		time.sleep(0.1)

#退回去回复原来动作
# def retrive(name):
# 	t = serial.Serial("/dev/ttyUSB0",9600)
# 	t.write(name.encode())
# 	while True:
# 		x = ""
# 		flag = True
# 		while t.inWaiting() > 0:
# 			str_in = t.read(t.inWaiting())
# 			# print(str_in)
# 			# print(type(str_in))
# 			x += str(str_in)
# 			time.sleep(0.01)
# 			flag = False
# 		if flag == False:
# 			# print("in if")
# 			x = x.split('\'')[1]
# 			print("res"+str(x))
# 			if x == "o":
# 				break;
# 		time.sleep(0.1)
# 	return "o"
	
if __name__ == '__main__':
	# good_arm(1)
	init()
	time.sleep(1)
	good_arm(3)
	time.sleep(1)
	gesture()

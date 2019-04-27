# -- coding: utf-8 --
import serial
import time
def send(name):									#pi->win:切割，图像识别，判空
	t = serial.Serial("/dev/ttyUSB2",9600)
	t.write(name.encode())

def send_receive(name):							#pi<->win:拍照
	t = serial.Serial("/dev/ttyUSB2",9600)
	t.write(name.encode())
	while True:
		x = ""
		flag = True
		# while t.inWaiting() > 0:
		# 	str_in = t.read(t.inWaiting())
		# 	x += str(str_in)
		# 	time.sleep(0.01)
		# 	flag = False
		# if flag == False:
		# 	x = x.split('\'')[1]
		# 	print("res"+str(x))
		# 	if x == "k":
		# 		break;
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			st = str(str_in).split('\'')[1]
			print(st)
			x += st
			print(x)
			time.sleep(0.01)
			flag = False
		if flag == False:
			# x = x.split('\'')[1]
			print("res"+str(x))
			if x == "k":
				break;
		time.sleep(0.1)

def get_outcome(name):							#pi<->win:结果传输
	t = serial.Serial("/dev/ttyUSB2",9600)
	t.write(name.encode())
	while True:
		x = ""
		flag = True
		# while t.inWaiting() > 0:
		# 	str_in = t.read(t.inWaiting())
		# 	x += str(str_in)
		# 	time.sleep(0.01)
		# 	flag = False
		# if flag == False:
		# 	print("outcome = "+x)
		# 	x = x.split('\"')[1]
		# 	print("res = "+str(x))
		# 	print(type(x))
		# 	return x
		while t.inWaiting() > 0:
			str_in = t.read(t.inWaiting())
			ch = str(str_in).split('\"')[1]
			x += ch
			time.sleep(0.01)
			flag = False
		if flag == False:
			print("outcome = "+x)
			# x = x.split('\"')[1]
			print("res = "+str(x))
			print(type(x))
			return x
		time.sleep(0.1)
# def receive():									#pi<-win
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

if __name__ == '__main__':
	send()
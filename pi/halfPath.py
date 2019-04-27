# -- coding: utf-8          --
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)	 #f,h
GPIO.setup(40,GPIO.OUT)  #e,l
GPIO.setup(16,GPIO.OUT)	 #high/low
GPIO.setup(18,GPIO.OUT)  #en
GPIO.setup(22,GPIO.OUT)  #entacking

def start2():
	GPIO.output(16,0)
	GPIO.output(18,1)

def stop():
	GPIO.output(18,0)

def forward(x):			#前走半步
	GPIO.output(22,0)
	t = 0.5
	# if type == '1' or type == '3':
	# 	t = 0.85
	# elif type == '2':
	# 	t = 0.5
	if x == 4:
		GPIO.output(37,1)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		print("e")
	elif x == 7:
		GPIO.output(37,0)
		GPIO.output(40,0)
		start2()
		time.sleep(t)
		stop()
		print("n")

	elif x == 5:
		GPIO.output(37,0)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		print("w")

	elif x == 2:
		GPIO.output(37,1)
		GPIO.output(40,0)
		start2()
		time.sleep(t)
		stop()
		print("s")

def back(x):			#退走半步
	GPIO.output(22,0)
	t = 0.5
	# print("back")
	# print("x" +str(x))
	# print(type(x))
	# if type == '1' or type == '3':
	# 	t = 0.85
	# elif type == '2':
	# 	t = 0.5
	if x == 4:
		GPIO.output(37,0)
		GPIO.output(40,1)
		# time.sleep(1)
		start2()
		time.sleep(t)
		stop()
		print("w")
	elif x == 7:
		GPIO.output(37,1)
		GPIO.output(40,0)
		start2()
		time.sleep(t)
		stop()
		print("s")

	elif x == 5:
		GPIO.output(37,1)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		print("e")

	elif x == 2:
		GPIO.output(37,0)
		GPIO.output(40,0)
		start2()
		time.sleep(t)
		stop()
		print("n")

def left(x):			#向左走半格
	GPIO.output(22,0)
	t = 0.82
	print("left")
	if x == 4:
		GPIO.output(37,0)
		GPIO.output(40,0)
		time.sleep(1)
		start2()
		time.sleep(t)
		stop()
		# time.sleep(1)
		print("n")
		
	elif x == 7:
		GPIO.output(37,0)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		print("w")

	elif x == 5:
		GPIO.output(37,1)
		GPIO.output(40,0)
		start2()
		time.sleep(t)
		stop()
		print("s")
		

	elif x == 2:
		GPIO.output(37,1)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		print("e")

def right(x):			#向右走半格
	GPIO.output(22,0)
	print("right")
	t = 0.82
	if x == 4:
		GPIO.output(37,1)
		GPIO.output(40,0)
		time.sleep(1)
		start2()
		time.sleep(t)
		stop()
		print("s")
		

		# print(x)

	elif x == 7:
		GPIO.output(37,1)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		print("e")

		# print(x)


	elif x == 5:
		GPIO.output(37,0)
		GPIO.output(40,0)
		start2()
		time.sleep(t)
		stop()
		print("n")

		# print(x)


	elif x == 2:
		GPIO.output(37,0)
		GPIO.output(40,1)
		start2()
		time.sleep(t)
		stop()
		# print(x)
		print("w")


if __name__ == '__main__':
	while True:
		# GPIO.output(22,1)
		name = input("input:")
		name = int(name)
		# print(name)
		# forward(name)
		# time.sleep(1)
		
		# right(name)
		# time.sleep(1)
		# forward(name)
		# time.sleep(1)
		left(name)
		time.sleep(1)
		forward(name)
		time.sleep(1)		
		back(name)
		time.sleep(1)
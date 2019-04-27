# -- coding: utf-8 --
import RPi.GPIO as GPIO
import ctypes
import time
so = ctypes.cdll.LoadLibrary   
lib = so("./libpycall1.so")

#list_goods = [[4,2],[7,4],[5,7],[2,5]]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.IN)   #count
GPIO.setup(37,GPIO.OUT)	 #f,h
GPIO.setup(40,GPIO.OUT)  #e,l
GPIO.setup(32,GPIO.OUT)  #en

def start():
	GPIO.output(32,1)

def stop():
	GPIO.output(32,0)

def walk(p):
	print(len(p))	
	for i in range(0,len(p),2):
		if p[i] == '1':
			print("north") 
			GPIO.output(37,0) #f
			GPIO.output(40,0) #e
		if p[i] == '2':
			print("west")
			GPIO.output(37,0) #f
			GPIO.output(40,1) #e
		if p[i] == '3':
			print("south")
			GPIO.output(37,1) #f
			GPIO.output(40,0) #e
		if p[i] == '4':
			print("east")
			GPIO.output(37,1) #f
			GPIO.output(40,1) #e
		tempary = int(p[i+1])
		start()
		time.sleep(0.5)
		while True:
			channel = GPIO.wait_for_edge(36, GPIO.RISING)
			if channel == None:
				print("none")
			else:
				tempary -= 1
				print(tempary)
				if(tempary == 0):
					stop()		
					print("run over")
					break;
				time.sleep(0.5)

if __name__ == '__main__':
	print("please enter original site")
	temp0 = raw_input()
	cmd0 = temp0.split()
	currentx = int(cmd0[0])
	currenty = int(cmd0[1])
	while True:
		print("please enter aim site")
		temp = raw_input()
		cmd = temp.split()
		print(cmd)
		ax = int(cmd[0])
		ay = int(cmd[1])
		if(ax>= 3 and ax<=6 and ay>=3 and ay<=6):
			continue
		p = lib.display_int(ax,ay,currentx,currenty)
		p = str(p)
		print("p = " + str(p))
		walk(p)
		currentx = ax
		currenty = ay
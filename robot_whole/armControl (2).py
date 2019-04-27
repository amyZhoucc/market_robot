# -- coding: utf-8 --
import RPi.GPIO as GPIO

def good_arm(name):
	if name == 1:
		print("C")
	elif name == 2:
		print("D")
	elif name == 3:
		print("A")
	elif name == 4:
		print("B")
		
def ware_arm(name):		#货仓拍照，共有4套动作，分别表示4个方向
	if name == 'a':
		print(1)
	elif name == 'b':
		print(2)
	elif name == 'c':
		print(3)
	elif name == 'd':
		print(4)

def rotate():			#旋转

def grab_good(name):  	#抓取货物
	print(name)

def place_good():		#放置货物
	print(name)

if __name__ == '__main__':
	good_arm(1)
	ware_arm('a')
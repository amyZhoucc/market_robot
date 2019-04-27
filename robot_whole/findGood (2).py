# -- coding: utf-8 --
import numpy as np
import cv2
#import runControl
#import armControl
from Camera import Camera_init
import retrain_test
import time
currentx = 0
currenty = 0											#起始位置为(0,0)
picture = []											#存放4张照片
pic_good = [[]for i in range(4)]						#存放4组，12张货物图片1-1，1-2....
result = {}												#字典形式返回识别结果 '4-2':'apple'类似
def findGood():
	global currentx,currenty							#设为全局变量，存放当前位置
	i = 0
	camera = Camera_init()								#摄像头初始化
	camera.cap = cap = cv2.VideoCapture(0)
	time.sleep(3)
	list_goods = [(4,2),(7,4),(5,7),(2,5)]  #货物坐标
	for good in list_goods:
		i += 1
		print("移动进程")
		#runControl.runControl(currentx,currenty,good[0],good[1]) #前往位置

		path = 'image/image_goods/'+str(i)
		#print(path)
		print("货物拍照进程：")
		picture.append(camera.use_Camera(path))	       	#拍摄照片，传回照片

		currentx = good[0]							   
		currenty = good[1]								#更新当前路径
		print("curx = "+str(currentx) + " cury = "+str(currenty))

		print("机械臂移动进程")
		#armControl.good_arm(i)							#机械臂旋转，参数为整型
		
	pic_good = camera.split_Camera1(picture)		#图片切割，获得切割后的图片
	print("货物识别进程:")
	result = retrain_test.label_images()			#图像识别的结果
	print(result)
	del(camera)
	return result

if __name__ == '__main__':
	findGood()

# -- coding: utf-8 --
import numpy as np
import cv2
import runControl
import armControl
import send
# from Camera import Camera_init
# import retrain_test
import time
currentx = 0
currenty = 2											#起始位置为(0,0)
# picture = []											#存放4张照片
# pic_good = [[]for i in range(4)]						#存放4组，12张货物图片1-1，1-2....
# result = {}											#字典形式返回识别结果 '4-2':'apple'类似
def findGood():
	global currentx,currenty							#设为全局变量，存放当前位置
	i = 0
	# camera = Camera_init()							#摄像头初始化
	# camera.cap = cap = cv2.VideoCapture(0)
	# send.send('0')									#pi->window摄像头初始化
	list_goods = [(4,2),(7,4),(5,7),(2,5)]  			#货物坐标
	for good in list_goods:
		i += 1
		print("移动进程")
		print("机械臂移动过程")							#机械臂旋转，参数为整型
		armControl.good_arm(i)
		
		runControl.runControl(currentx,currenty,good[0],good[1]) #前往位置
		
		# print("机械臂移动过程")							#机械臂旋转，参数为整型
		# armControl.good_arm(i)
		time.sleep(1)
		# path = 'test/image_goods/'+str(i)				#测试文件放置

		# path = 'image/image_goods/'+str(i)				
		# print(path)
		print("货物拍照进程：")
		send.send_receive("p"+str(i))					#pi<->window传输路径 p1，p2等
		# picture.append(camera.use_Camera(path))		#拍摄照片，传回照片

		currentx = good[0]							   
		currenty = good[1]								#更新当前路径
		print("curx = "+str(currentx) + " cury = "+str(currenty))

		time.sleep(1)
	send.send('1')										#pi->window图片切割，获得切割后的图片
	# pic_good = camera.split_Camera1(picture)		

	# #待修改的
	print("货物识别进程:")
	send.send('2')									#pi->window图像识别
	# result = retrain_test.label_images()			#图像识别的结果，格式为字典
	# print(result)
	# del(camera)
	# return result

if __name__ == '__main__':
	findGood()

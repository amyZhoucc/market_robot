# -- coding: utf-8 --
import numpy as np
import runControl
import armControl
# from Camera import Camera_init
import time
import cv2
import send
currentx = 2
currenty = 5								#初始位置为(0,4)
# picture = []								#存放拍的照片：每组结束之后，清空
# pic_ware = []								#存放切割后的照片：二维的列表
# empty_ware =[]								#存放空货架：二维列表
def scanStore():	
	global currentx,currenty				#设置为全局变量，存放当前位置
	# camera = Camera_init()					#摄像头初始化
	# camera.cap = cap = cv2.VideoCapture(0)
	line = 'a'
	list_ware =[[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)],
				[(9,0),(9,1),(9,2),(9,3),(9,4),(9,5)],
				[(9,9),(8,9),(7,9),(6,9),(5,9),(4,9)],
				[(0,9),(0,8),(0,7),(0,6),(0,5),(0,4)]]   #货架位置
	for wares in list_ware:
		i = 1
		print("机械臂转动进程")
		armControl.ware_arm(line)						#参数值为char类型
		for ware in wares:
			print("移动进程")
			runControl.runControl(currentx,currenty,ware[0],ware[1])
			time.sleep(1)
			
			name = line +str(i) 
			print("货仓拍照进程")
			send.send_receive(name)						#pi<->win拍摄照片，参数为a1,a2等
			# picture.append(camera.use_Camera(name))	#拍摄照片，传回照片
			i += 1
			currentx = ware[0]							#更新当前位置
			currenty = ware[1]  
			# print("curx = "+str(currentx) + " cury = "+str(currenty))
		time.sleep(1)

		# pic_ware.append(camera.split_Camera2(picture,line))#图片切割成上下两部分

		# print("判空进程")
		# empty_ware.append(Empty.judgeEmpty(line))		   #判空，返回列表，压入列表['a1-L','a4-H','a3-L']

		line = ord(line)
		line += 1
		line = chr(line)									#更新货架标志a,b,c,d
	
	print("图片切割进程")
	send.send('3')									#pi->win图片切割
	time.sleep(1)

	print("判空进程")
	send.send('4')									#pi->win图片判空
		# print(empty_ware)
		# picture.clear()
	# del(camera)
	# return empty_ware
		
if __name__ == '__main__':
	scanStore()

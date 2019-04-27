# -- coding: utf-8 --
import cv2
import time

# #使用相机
# def use_Camera(i):
# 	cap = cv2.VideoCapture(0) 	# 读取摄像头，0表示系统默认摄像头
# 	ret, photo = cap.read()		# 读取图像
# 	time.sleep(1)
# 	#cv2.imshow('Take Photo', photo)
# 	# 将图像传送至窗口

# 	filename = i + ".jpg"
# 	# 以当前参数存储
# 	cv2.imwrite(filename, photo)	# 保存位置
# 	return filename

# def stop():
# 	cap.release()

# #货物图片切割（一起切割）
# def split_Camera1(pictures):
# 	i = 0
# 	pic_goods = [[]for i in range(4)]  #构建二维列表，共4行

# 	for picture in pictures:
# 		temp = cv2.imread(picture)	   #读取图片

# 		#print(picture)
# 		picture.split('.')
# 		paths = picture.split('.')[0].split('/')
# 		path = paths[0]+'/'+paths[1]

# 		temp1 = temp[:,0:220]          #切割第一张图片,参数待修改
# 		filename1 = path+'/'+'separate_goods/'+paths[2]+ "-" + "1" + ".jpg" #命名
# 		#print(filename1)
# 		cv2.imwrite(filename1, temp1)  #写入
# 		# cv2.imshow("pic",temp1)	   #显示图片
# 		# cv2.waitKey(0)			   #等待

# 		temp2 = temp[:,220:440]        #切割第二张图片，参数待修改
# 		filename2 = path+'/'+'separate_goods/'+paths[2]+ "-" + "2" + ".jpg"
# 		#print(filename2)
# 		cv2.imwrite(filename2, temp2)
# 		# cv2.imshow("pic", temp2)
# 		# cv2.waitKey(0)

# 		temp3 = temp[:,440:640]		    #切割第三张图片，参数待修改
# 		filename3 = path+'/'+'separate_goods/'+paths[2]+ "-" + "3" + ".jpg"
# 		#print(filename3)
# 		cv2.imwrite(filename3, temp3)
# 		# cv2.imshow("pic", temp3)
# 		# cv2.waitKey(0)

# 		pic_goods[i].append(filename1)	 #放入列表中
# 		pic_goods[i].append(filename2)
# 		pic_goods[i].append(filename3)
# 		i += 1
# 	return pic_goods					 #返回该列表

# #货架图片切割（一组切割）
# def split_Camera2(pictures,line):
# 	i = 0
# 	pic_wares = [[]for i in range(6)]  #构建二维列表，共行

# 	for picture in pictures:
# 		temp = cv2.imread(picture)	   #读取图片
# 		picture.split('.')
# 		temp1 = temp[:,0:220]          #切割上层图片，参数待修改
# 		paths = picture.split('.')[0].split('/')
# 		path = paths[0]  + "/" + paths[1]
# 		filename1 = path + "/" + "ware_"+ line + "/" + paths[2]+"-" + "H" + ".jpg" #命名
# 		cv2.imwrite(filename1, temp1)  #写入
# 		cv2.imshow("pic",temp1)	   #显示图片
# 		cv2.waitKey(0)			   #等待

# 		temp2 = temp[:,220:440]        #切割下层图片，参数待修改
# 		filename2 = path + "/" + "ware_" + line+"/"+paths[2]+"-" + "L" + ".jpg"
# 		cv2.imwrite(filename2, temp2)
# 		cv2.imshow("pic", temp2)
# 		cv2.waitKey(0)

# 		pic_wares[i].append(filename1)	 #放入列表中
# 		pic_wares[i].append(filename2)
# 		i += 1
# 	return pic_wares					 #返回该列表	

class Camera_init(object):
	"""docstring for Carera"""
	def __init__(self):
		time.sleep(0.1)
		# self.cap = cv2.VideoCapture(0) 	# 读取摄像头，0表示系统默认摄像头
	def use_Camera(self,i):
		# cap = cv2.VideoCapture(0) 	# 读取摄像头，0表示系统默认摄像头
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		ret, photo = self.cap.read()		# 读取图像
		time.sleep(1)
		#cv2.imshow('Take Photo', photo)
		# 将图像传送至窗口
		filename = i + ".jpg"
		# 以当前参数存储
		cv2.imwrite(filename, photo)	# 保存位置
		return filename

	def stop():
		cap.release()

	#货物图片切割（一起切割）
	def split_Camera1(self,pictures):
		i = 0
		pic_goods = [[]for i in range(4)]  #构建二维列表，共4行

		for picture in pictures:
			temp = cv2.imread(picture)	   #读取图片

			#print(picture)
			picture.split('.')
			paths = picture.split('.')[0].split('/')
			path = paths[0]+'/'+paths[1]

			temp1 = temp[:,0:220]          #切割第一张图片,参数待修改
			filename1 = path+'/'+'separate_goods/'+paths[2]+ "-" + "1" + ".jpg" #命名
			#print(filename1)
			cv2.imwrite(filename1, temp1)  #写入
			# cv2.imshow("pic",temp1)	   #显示图片
			# cv2.waitKey(0)			   #等待

			temp2 = temp[:,220:440]        #切割第二张图片，参数待修改
			filename2 = path+'/'+'separate_goods/'+paths[2]+ "-" + "2" + ".jpg"
			#print(filename2)
			cv2.imwrite(filename2, temp2)
			# cv2.imshow("pic", temp2)
			# cv2.waitKey(0)

			temp3 = temp[:,440:640]		    #切割第三张图片，参数待修改
			filename3 = path+'/'+'separate_goods/'+paths[2]+ "-" + "3" + ".jpg"
			#print(filename3)
			cv2.imwrite(filename3, temp3)
			# cv2.imshow("pic", temp3)
			# cv2.waitKey(0)

			pic_goods[i].append(filename1)	 #放入列表中
			pic_goods[i].append(filename2)
			pic_goods[i].append(filename3)
			i += 1
		return pic_goods					 #返回该列表

	#货架图片切割（一组切割）
	def split_Camera2(self,pictures,line):
		i = 0
		pic_wares = [[]for i in range(6)]  #构建二维列表，共行

		for picture in pictures:
			temp = cv2.imread(picture)	   #读取图片
			picture.split('.')
			temp1 = temp[:,0:220]          #切割上层图片，参数待修改
			paths = picture.split('.')[0].split('/')
			path = paths[0]  + "/" + paths[1]
			filename1 = path + "/" + "ware_"+ line + "/" + paths[2]+"-" + "H" + ".jpg" #命名
			cv2.imwrite(filename1, temp1)  #写入
			# cv2.imshow("pic",temp1)	   #显示图片
			# cv2.waitKey(0)			   #等待

			temp2 = temp[:,220:440]        #切割下层图片，参数待修改
			filename2 = path + "/" + "ware_" + line+"/"+paths[2]+"-" + "L" + ".jpg"
			cv2.imwrite(filename2, temp2)
			# cv2.imshow("pic", temp2)
			# cv2.waitKey(0)

			pic_wares[i].append(filename1)	 #放入列表中
			pic_wares[i].append(filename2)
			i += 1
		return pic_wares					 #返回该列表	
	def __del__(self):
		self.cap.release()
		print("over")

if __name__ == '__main__':
	camera = Camera_init()								#摄像头初始化
	camera.cap = cap = cv2.VideoCapture(1)
	path = 'image/image_goods/'+str(1)
	camera.use_Camera(path)

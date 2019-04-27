# -- coding: utf-8 --
import numpy as np
import cv2
import os
def judgeEmpty(line):  					#line为当前货架，有a,b,c,d
	pic_area = []      					#存放图片以及对应的物体面积
	empty_ware = []    					#存放每次的三个空货架
	for root, dirs, files in os.walk("./image/image_wares/ware_"+line+'/'):			#找到当前货架的图片位置
		len1 = len(files)				#获取当前文件夹图片个数
		for file in files[:len1-1]:	#windows下默认有一个pb文件，要将其删去，但是linx下无
			img_dir = str(os.path.join(root, file))   #拼接图片完整路径（相对于该函数的路径）
			img = cv2.imread(img_dir)    #import
			# cv2.imshow("img",img)
			# cv2.waitKey(0)
			img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #gray
			binary = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,2)  #binary-reverse
			bin,contours, hierarchy = cv2.findContours(binary,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)               #findcontours
			max_area = 0
			if contours != []:
				for index in contours:
					x1 = []
					x2 = []
					y1 = []
					y2 = []
					for index2 in index:
						x1.append(index2[0][0])
						x2.append(index2[0][0])
						y1.append(index2[0][1])
						y2.append(index2[0][1])
					x1.sort(reverse=True)
					x2.sort()
					y1.sort(reverse=True)
					y2.sort()
					area = (x1[0] - x2[0]) * (y1[0] - y2[0])
					if max_area < area :
						maxx = x1[0]
						minx = x2[0]
						maxy = y1[0]
						miny = y2[0]
						max_area = area
				# cv2.rectangle(img, (minx,miny), (maxx, maxy), (255,0,0), 1)
				# cv2.namedWindow('img3',cv2.WINDOW_NORMAL)
				# cv2.imshow("img3", img)
				# cv2.waitKey(0)
			else:
				print(0)
			paths = img_dir.split('/')
			path = paths[4].split('.')[0]
			d = (path,max_area)					    #创建元组，格式为('c1-L',area)
			pic_area.append(d)						#将元组放入列表中

		pic_area.sort(key=lambda x:x[1])			#排序
		for i in range(0,3):
			empty_ware.append(pic_area[i][0])		#取出area最小的三个，放入列表中
	# print(pic_area)
	print(empty_ware)
	return empty_ware								#返回空货架列表


if __name__ == '__main__':
	judgeEmpty('a')
# ['a1-L', 'a2-L', 'a3-L']
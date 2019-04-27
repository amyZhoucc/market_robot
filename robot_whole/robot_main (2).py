# -- coding: utf-8 --
import numpy as np
import cv2
import findGood
import scanStore
import findRoot
import planSite
import grab_place
good_result = {}      					#返回货物的标号和名字，类型字典 eg:'4-2':apple
empty_ware = [[]for i in range(4)]		#返回空货架的标号，类型二维列表 eg:'a1-L'
good_site = {}							#类型字典    eg: (7, 4): ['d', 'c', 'c']
ware_site = {}							#类型字典    eg: 'c': [(7, 9), (5, 9), (4, 9)]
planningSite  = []
if __name__ == '__main__':
	print("货物扫描函数")
	good_result = findGood.findGood()	
	print("货仓扫描函数")
	empty_ware = scanStore.scanStore()
	print("货物列表整理函数")
	good_site = findRoot.findGoodRoot(good_result)	#返回货物的坐标，类型字典
	print("货仓列表整理函数")
	ware_site = findRoot.findStoreRoot(empty_ware)	#返回空货架的坐标，类型字典
	print("路径规划函数")
	planningSite = planSite.runTo(good_site,ware_site)
	print("货物抓取和放置函数")
	grab_place.grabPlace(planningSite,good_result,empty_ware)  #参数传递为规划的路径，货物名称（包含位置），空货架标号（包括上下层）
	

	
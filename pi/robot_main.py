# -- coding: utf-8 --
# import retrain_test
# import multiprocessing as mp
import numpy as np
import findGood
import scanStore
import findRoot
import planSite
import grab_place
import armControl
# good_result = {}      					#返回货物的标号和名字，类型字典 eg:'4-2':apple
empty_ware = [[]for i in range(4)]		#返回空货架的标号，类型二维列表 eg:'a1-L'
good_site = {}							#类型字典    eg: (7, 4): [{'d': 'green square-1'}, {'c': 'snow flower-2'}, {'c': 'apple-3'}]
ware_site = {}							#类型字典    eg: 'c': [((7, 9), 'H'), ((5, 9), 'H'), ((4, 9), 'H')]
planningSite  = []						#类型列表	eg: (2, 5, 'badminton-2'), (2, 0, 'H')

if __name__ == '__main__':
	# armControl.init()					#机械臂初始化动作
	# p1 = mp.Process(target = retrain_test.label_images,args=())

	print("货物扫描函数")
	findGood.findGood()

	# p1.start()				#货物识别进程
	
	print("货仓扫描函数")
	empty_ware = scanStore.scanStore()
	print("货物列表整理函数")
	good_site = findRoot.findGoodRoot()	#返回货物的坐标，类型字典
	print("货仓列表整理函数")
	ware_site = findRoot.findStoreRoot()	#返回空货架的坐标，类型字典
	print("路径规划函数")
	planningSite = planSite.runTo(good_site,ware_site)
	armControl.init()					#机械臂初始化动作
	print("货物抓取和放置函数")
	grab_place.grabPlace(planningSite)  #参数传递为规划的路径
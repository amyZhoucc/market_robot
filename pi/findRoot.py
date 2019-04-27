# -- coding: utf-8 --
import numpy as np
import send
import time
# def use_file():
# 	res = 'res.bat'
# 	fileHandle = open (res) 
# 	fileList = fileHandle.readlines() 
# 	fileHandle.close()
# 	dir = eval(fileList[0])
# 	return dir

def findGoodRoot():
	time.sleep(2)
	dic = eval(send.get_outcome("6"))				#pi<->win读取货物，返回的是字符串，构建成字典
	goodsDic = {'1':(4,2),'2':(7,4),'3':(5,7),'4':(2,5)}
	root = {(2,5):[' ', ' ',' '],(7,4):[' ',' ',' '],(5,7):[' ',' ',' '],(4,2):[' ',' ',' ']}
	print(dic)
	print(type(dic))
	for keys in dic:
		key = keys.split('-')[0]
		if key in goodsDic.keys():
			temp = int(keys.split('-')[1]) - 1
			root[goodsDic[key]][temp]= goodSite(dic[keys],keys.split('-')[1])  
	print(root)
	return root

def findStoreRoot():
	time.sleep(2)
	ware_str = send.get_outcome("5")			#读取空货架，返回的是字符串
	print(ware_str)
	lists = ware_str.split(' ')					#切割按照',',得到的是list
	print(lists)
	wareDic = {'a1':(0,0),'a2':(1,0),'a3':(2,0),'a4':(3,0),'a5':(4,0),'a6':(5,0),
				 'b1':(9,0),'b2':(9,1),'b3':(9,2),'b4':(9,3),'b5':(9,4),'b6':(9,5),
				 'c1':(9,9),'c2':(8,9),'c3':(7,9),'c4':(6,9),'c5':(5,9),'c6':(4,9),
				 'd1':(0,9),'d2':(0,8),'d3':(0,7),'d4':(0,6),'d5':(0,5),'d6':(0,4)}
	root = {'a':[],'b':[],'c':[],'d':[]}
	for store in lists:
		# print(store)
		# key = store.split('-')[0]
		key = (store.split('-')[0]).split('\'')[1]
		if key in wareDic.keys():
			root[key[0]].append((wareDic[key],(store.split('-')[1]).split('\'')[0])) 
		else:
			continue
	print(root)
	return root

def goodSite(name,site):
	if name == 'redsquare':
		return {'a':name+'-'+site}
	elif name == 'yakult':
		return {'a':name+'-'+site}
	elif name == 'badminton':
		return {'a':name+'-'+site}
	elif name == 'yellowsquare':
		return {'b':name+'-'+site}
	elif name == 'sww':
		return {'b':name+'-'+site}
	elif name == 'steelwool':
		return {'b':name+'-'+site}
	elif name == 'bluesquare':
		return {'c':name+'-'+site}
	elif name == 'snowflower':
		return {'c':name+'-'+site}
	elif name == 'apple':
		return {'c':name+'-'+site}
	elif name == 'greensquare':
		return {'d':name+'-'+site}
	elif name == 'sprite':
		return {'d':name+'-'+site}
	elif name == 'tennisball':
		return {'d':name+'-'+site}
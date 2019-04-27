# -- coding: utf-8 --
import numpy as np

def use_file():
	res = 'res.bat'
	fileHandle = open (res) 
	fileList = fileHandle.readlines() 
	fileHandle.close()
	dir = eval(fileList[0])
	return dir

def findGoodRoot():
	dic = use_file()
	goodsDic = {'1':(4,2),'2':(7,4),'3':(5,7),'4':(2,5)}
	root = {(2,5):[' ', ' ',' '],(7,4):[' ',' ',' '],(5,7):[' ',' ',' '],(4,2):[' ',' ',' ']}
	for keys in dic:
		key = keys.split('-')[0]
		if key in goodsDic.keys():
			temp = int(keys.split('-')[1]) - 1
			root[goodsDic[key]][temp]= goodSite(dic[keys],keys.split('-')[1])  
	print(root)
	return root

def findStoreRoot(lists):
	wareDic = {'a1':(0,0),'a2':(1,0),'a3':(2,0),'a4':(3,0),'a5':(4,0),'a6':(5,0),
				 'b1':(9,0),'b2':(9,1),'b3':(9,2),'b4':(9,3),'b5':(9,4),'b6':(9,5),
				 'c1':(9,9),'c2':(8,9),'c3':(7,9),'c4':(6,9),'c5':(5,9),'c6':(4,9),
				 'd1':(0,9),'d2':(0,8),'d3':(0,7),'d4':(0,6),'d5':(0,5),'d6':(0,4)}
	root = {'a':[],'b':[],'c':[],'d':[]}
	for list in lists:
		for store in list:
			key = store.split('-')[0]
			if key in wareDic.keys():
				root[key[0]].append((wareDic[key],store.split('-')[1])) 
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

if __name__ == '__main__':
	dic = {'1-1': 'redsquare', '1-2': 'tennis ball', '1-3': 'sprite', '2-1': 'green square','2-2': 'snow flower', '2-3': 'apple', '3-1': 'blue square', '3-2': 'steel wool', '3-3': 'sww', '4-1': 'yellow square','4-2': 'badminton','4-3': 'yakult'}	
	findGoodRoot()
	lists = [['a1-H', 'a2-H', 'a3-H'], ['b1-H', 'b1-L', 'b2-H'], ['c3-H', 'c5-H', 'c6-H'], ['d3-H', 'd5-H', 'd1-H']]
	findStoreRoot(lists)
	#use_file()

#{(7, 4): [{'d': 'green square-1'}, {'c': 'snow flower-2'}, {'c': 'apple-3'}], (4, 2): [{'a': 'red quare-1'}, {'d': 'tennis ball-2'}, {'d': 'sprite-3'}], (2, 5): [{'b': 'yellow square-1'}, {'a': 'badminton-2'}, {'a': 'yakult-3'}], (5, 7): [{'c': 'blue square-1'}, {'b': 'steel wool-2'}, {'b': 'sww-3'}]}
#{'c': [((7, 9), 'H'), ((5, 9), 'H'), ((4, 9), 'H')], 'a': [((0, 0), 'H'), ((1, 0), 'H'), ((2, 0), 'H')], 'b': [((9, 0), 'H'), ((9, 0), 'L'), ((9, 1), 'H')], 'd': [((0, 7), 'H'), ((0, 5), 'H'), ((0, 9), 'H')]}
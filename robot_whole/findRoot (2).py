# -- coding: utf-8 --
import numpy as np
def findGoodRoot(dic):
	goodsDic = {'1':(4,2),'2':(7,4),'3':(5,7),'4':(2,5)}
	root = {(2,5):[' ', ' ',' '],(7,4):[' ',' ',' '],(5,7):[' ',' ',' '],(4,2):[' ',' ',' ']}
	for keys in dic:
		key = keys.split('-')[0]
		if key in goodsDic.keys():
			temp = int(keys.split('-')[1]) - 1
			root[goodsDic[key]][temp]= goodSite(dic[keys]) 
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
				root[key[0]].append(wareDic[key]) 
			else:
				continue
	print(root)
	return root

def goodSite(name):
	if name == 'red quare':
		return ('a')
	elif name == 'yakult':
		return 'a'
	elif name == 'badminton':
		return 'a'
	elif name == 'yellow square':
		return 'b'
	elif name == 'sww':
		return 'b'
	elif name == 'steel wool':
		return 'b'
	elif name == 'blue square':
		return 'c'
	elif name == 'snow flower':
		return 'c'
	elif name == 'apple':
		return 'c'
	elif name == 'green square':
		return 'd'
	elif name == 'sprite':
		return 'd'
	elif name == 'tennis ball':
		return 'd'

if __name__ == '__main__':
	dic = {'1-1': 'red quare', '1-2': 'tennis ball', '1-3': 'sprite', '2-1': 'green square','2-2': 'snow flower', '2-3': 'apple', '3-1': 'blue square', '3-2': 'steel wool', '3-3': 'sww', '4-1': 'yellow square','4-2': 'badminton','4-3': 'yakult'}	
	findGoodRoot(dic)
	lists = [['a1-H', 'a2-H', 'a3-H'], ['b1-H', 'b1-L', 'b2-H'], ['c3-H', 'c5-H', 'c6-H'], ['d3-H', 'd5-H', 'd1-H']]
	findStoreRoot(lists)


# {(7, 4): ['d', 'c', 'c'], (4, 2): ['a', 'd', 'd'], (2, 5): ['b', 'a', 'a'], (5, 7): ['c', 'b', 'b']}
# {'c': [(7, 9), (5, 9), (4, 9)], 'b': [(9, 0), (9, 0), (9, 1)], 'a': [(0, 0), (1, 0), (2, 0)], 'd': [(0, 7), (0, 5), (0, 9)]}

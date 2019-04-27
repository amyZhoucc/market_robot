# -- coding: utf-8 --
import ctypes
so = ctypes.cdll.LoadLibrary 
lib = so("./libpycall1.so")
planning_path = []
def runTo(good_Dir,ware_Dir):
	currentx = 0
	currenty = 4
	while (len(good_Dir[(2,5)])!=0) or (len(good_Dir[(4,2)])!= 0) or (len(good_Dir[(7,4)])!=0) or (len(good_Dir[(5,7)])!=0):
		minlen_Good = 999
		for key in good_Dir:
			if len(good_Dir[key]) == 0:
				continue
			# print(currentx)
			# print(currenty)
			templen_Good = lib.display_string(key[0],key[1],currentx,currenty)
			if templen_Good < minlen_Good:
				minlen_Good = templen_Good
				maxx = key[0]
				maxy = key[1]
		# planning_path.append((currentx,currenty))		#元组加入列表中
		c = selectGood(maxx,maxy,good_Dir)		#选择抓取的货物
		print(c)
		for key in c:
			planning_path.append((maxx,maxy,c[key]))   #元组加入列表中，为(x,y,'green square-1')
		good_Dir[(maxx,maxy)].remove(c)
		currentx = maxx
		currenty = maxy

		minlen_Ware = 999
		for ware in ware_Dir[key]:
			templen_Ware = lib.display_string(ware[0][0],ware[0][1],currentx,currenty)
			if templen_Ware < minlen_Ware:
				minlen_Ware = templen_Ware
				maxx = ware[0][0]
				maxy = ware[0][1]
				temp = ware[1]
		planning_path.append((maxx,maxy,temp))		#元组加入列表中,为(x,y,'L')
		ware_Dir[key].remove(((maxx,maxy),temp))
		currentx = maxx
		currenty = maxy
	print(planning_path)
	return planning_path


def selectGood(x,y,good_Dir):
	if x == 4:
		list = []
		for i in good_Dir[(4,2)]:
			for key in i:
				list.append(key)
		if 'a' in list:
			i = list.index('a')
			return good_Dir[(4,2)][i]
		elif 'b' in list:
			i = list.index('b')
			return good_Dir[(4,2)][i]

		elif 'd' in list:
			i = list.index('d')
			return good_Dir[(4,2)][i]
		elif 'c' in list:
			i = list.index('c')
			return good_Dir[(4,2)][i]

	if x == 7:
		list = []
		for i in good_Dir[(7,4)]:
			for key in i:
				list.append(key)

		if 'b' in list:
			i = list.index('b')
			return good_Dir[(7,4)][i]
		elif 'c' in list:
			i = list.index('c')
			return good_Dir[(7,4)][i]

		elif 'd' in list:
			i = list.index('d')
			return good_Dir[(7,4)][i]
		elif 'a' in list:
			i = list.index('a')
			return good_Dir[(7,4)][i]

	if x == 5:
		list = []
		for i in good_Dir[(5,7)]:
			for key in i:
				list.append(key)
		if 'c' in list:
			i = list.index('c')
			return good_Dir[(5,7)][i]
		elif 'd' in list:
			i = list.index('d')
			return good_Dir[(5,7)][i]

		elif 'b' in list:
			i = list.index('b')
			return good_Dir[(5,7)][i]
		elif 'a' in list:
			i = list.index('a')
			return good_Dir[(5,7)][i]
			
	if x == 2:
		list = []
		for i in good_Dir[(2,5)]:
			for key in i:
				list.append(key)

		if 'd' in list:
			i = list.index('d')
			return good_Dir[(2,5)][i]
		elif 'a' in list:
			i = list.index('a')
			return good_Dir[(2,5)][i]

		elif 'c' in list:
			i = list.index('c')
			return good_Dir[(2,5)][i]
		elif 'b' in list:
			i = list.index('b')
			return good_Dir[(2,5)][i]

if __name__ == '__main__':
	#good_Dir = {(2,5):['a','b','c'],(4,2):['c','d','c'],(7,4):['d','a','a'],(5,7):['b','b','d']}
	#good_Dir = {(7, 4): [('d', 'green square-1'), ('c', 'snow flower-2'), ('c', 'apple-3')], (4, 2): [('a', 'red quare-1'), ('d', 'tennis ball-2'), ('d', 'sprite-3')], (2, 5): [('b', 'yellow square-1'), ('a', 'badminton-2'), ('a', 'yakult-3')], (5, 7): [('c', 'blue square-1'), ('b', 'steel wool-2'), ('b', 'sww-3')]}
	good_Dir = {(7, 4): [{'d': 'greensquare-1'}, {'c': 'snowflower-2'}, {'c': 'apple-3'}], 
				(4, 2): [{'a': 'redsquare-1'}, {'d': 'tennisball-2'}, {'d': 'sprite-3'}], 
				(2, 5): [{'b': 'yellowsquare-1'}, {'a': 'badminton-2'}, {'a': 'yakult-3'}], 
				(5, 7): [{'c': 'bluesquare-1'}, {'b': 'steelwool-2'}, {'b': 'sww-3'}]}
	
	#ware_Dir = {'a':[(2,0),(3,0),(5,0)],'b':[(9,4),(9,2),(9,4)],'c':[(8,9),(4,9),(7,9)],'d':[(0,7),(0,4),(0,8)]}
	ware_Dir = {'c': [((7, 9), 'H'), ((5, 9), 'H'), ((4, 9), 'H')], 'a': [((0, 0), 'H'), ((1, 0), 'H'), ((2, 0), 'H')], 'b': [((9, 0), 'H'), ((9, 0), 'L'), ((9, 1), 'H')], 'd': [((0, 7), 'H'), ((0, 5), 'H'), ((0, 9), 'H')]}
	runTo(good_Dir,ware_Dir)
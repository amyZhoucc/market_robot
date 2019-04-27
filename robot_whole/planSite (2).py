# -- coding: utf-8 --
import ctypes
so = ctypes.cdll.LoadLibrary 
lib = so("./libpycall1.so")
currentx = 0
currenty = 4
planning_path = []
def runTo(good_Dir,ware_Dir):
	global currentx
	global currenty
	while (len(good_Dir[(2,5)])!=0) or (len(good_Dir[(4,2)])!= 0) or (len(good_Dir[(7,4)])!=0) or (len(good_Dir[(5,7)])!=0):
		minlen_Good = 999
		for key in good_Dir:
			if len(good_Dir[key]) == 0:
				continue
			templen_Good = lib.display_string(key[0],key[1],currentx,currenty)
			if templen_Good < minlen_Good:
				minlen_Good = templen_Good
				currentx = key[0]
				currenty = key[1]
		planning_path.append((currentx,currenty))		#元组加入列表中
		c = selectGood(currentx,currenty,good_Dir)		#选择抓取的货物
		good_Dir[(currentx,currenty)].remove(c)

		minlen_Ware = 999
		for ware in ware_Dir[c]:
			templen_Ware = lib.display_string(ware[0],ware[1],currentx,currenty)
			if templen_Ware < minlen_Ware:
				minlen_Ware = templen_Ware
				currentx = ware[0]
				currenty = ware[1]
		planning_path.append((currentx,currenty))		#元组加入列表中
		ware_Dir[c].remove((currentx,currenty))
	print(planning_path)


def selectGood(x,y,good_Dir):
	if x == 4:
		if ('a' in good_Dir[(x,y)]):
			return 'a'
		elif ('b' in good_Dir[(x,y)]):
			return 'b'
		elif ('d' in good_Dir[(x,y)]):
			return 'd'
		else:
			return 'c'
	if x == 7:
		if ('b' in good_Dir[(x,y)]):
			return 'b'
		elif ('c' in good_Dir[(x,y)]):
			return 'c'
		elif ('a' in good_Dir[(x,y)]):
			return 'a'
		else:
			return 'd'
	if x == 5:
		if ('c' in good_Dir[(x,y)]):
			return 'c'
		elif ('d' in good_Dir[(x,y)]):
			return 'd'
		elif ('b' in good_Dir[(x,y)]):
			return 'b'
		else:
			return 'a'
	if x == 2:
		if ('d' in good_Dir[(x,y)]):
			return 'd'
		elif 'a' in good_Dir[(x,y)]:
			return 'a'
		elif 'c' in good_Dir[(x,y)]:
			return 'c'
		else:
			return 'b'


if __name__ == '__main__':
	good_Dir = {(2,5):['a','b','c'],(4,2):['c','d','c'],(7,4):['d','a','a'],(5,7):['b','b','d']}
	ware_Dir = {'a':[(2,0),(3,0),(5,0)],'b':[(9,4),(9,2),(9,4)],'c':[(8,9),(4,9),(7,9)],'d':[(0,7),(0,4),(0,8)]}
	runTo(good_Dir,ware_Dir)
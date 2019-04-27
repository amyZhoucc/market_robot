# -- coding: utf-8 --
import armControl
import runControl
currentx = 0 
currenty = 4
def grabPlace(planningSite,good,empty_ware):
	global currentx
	global currenty
	i = 0
	for index in plannningRoute:
		runControl.runControl(currentx,currenty,index[0],index[1])
		if i % 2 == 0:						#抓取货物

			armControl.rotate(i)
			halfPath.halfPath()
			armControl.grab_good(i)
		else:								#放置货物
			
			armControl.place_good(i)
		i += 1

		currentx = index[0]				#更新路径
		currenty = index[1]

if __name__ == '__main__':
	grabPlace()
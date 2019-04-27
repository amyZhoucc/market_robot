# -- coding: utf-8 --
import armControl
import runControl
import halfPath
import time
currentx = 0
currenty = 4
def grabPlace(planningSite):
	print("root_path:")
	print(planningSite)
	print(type(planningSite))
	global currentx
	global currenty
	i = 0
	for index in planningSite:
		if i % 2 == 0:							#抓取货物
			runControl.runControl(currentx,currenty,index[0],index[1])   #到指定点
			print("货物抓取步骤")
			if index[0] == 4:
				dir = 1
			elif index[0] == 7:
				dir = 2
			elif index[0] == 5:
				dir = 3
			elif index[0] == 2:
				dir = 4
			
			#机械臂动作和行进是同步进行的，需要进行串口通信：arduino发ok给树莓派
			print("机械臂准备工作")
			armControl.good_arm(dir)		#机械臂抓取的准备工作——转向
			time.sleep(1)						#动作完成后延时1s
			sit = armControl.gesture()		#准备工作——准备抓取动作
			
			if index[2].split('-')[1] == '1':	#根据需要向左或者右，走半步
				print("向左走半步")
				halfPath.left(index[0])
			elif index[2].split('-')[1] == '3':
				print("向右走半步")
				halfPath.right(index[0])
			# time.sleep(1)						#左右半步走完之后，延时1s
			
			print("向前走半步")
			halfPath.forward(index[0])			#走半步
			# time.sleep(1)						#走半步之后，延时1s

			iden = good_identify(index[2].split('-')[0])
			print("抓取货物动作")			
			sit = armControl.grab_good(iden)			#机械臂根据不同的物体，做不同的动作，传输的是物品对应的编号

			print("向后退半步")
			halfPath.back(index[0])				#退半步
			# time.sleep(1)						#退半步之后，延时1s
			
			if index[2].split('-')[1] == '1':	#根据需要向左或者右，退半步
				print("向右退半步")
				halfPath.right(index[0])
			elif index[2].split('-')[1] == '3':
				print("向左退半步")
				halfPath.left(index[0])
			# time.sleep(1)						#左右半步退完之后，延时1s

			currentx = index[0]					#更新当前路径
			currenty = index[1]

		else:									#放置货物
			if index[0] >= 0 and index[0] <= 5 and index[1] == 0:
				dir = 'a'					#放到A货仓
				x = index[0]
				y = index[1] + 1
			elif index[0] == 9 and index[1] >= 0 and index[1] <= 5:
				dir = 'b'					#放到B货仓
				x = index[0] - 1
				y = index[1]
			elif index[0] >= 4 and index[0] <= 9 and index[1] == 9:
				dir = 'c'					#放到C货仓
				x = index[0]
				y = index[1] - 1
			elif index[0] == 0 and index[1] >= 4 and index[1] <= 9:
				dir = 'd'					#放到D货仓
				x = index[0] + 1
				y = index[1]
			else:
				continue
			runControl.runControl(currentx,currenty,x,y)   #到指定点
			print("货物放置动作")

			print("机械臂准备工作")
			armControl.ware_arm(dir)						#机械臂准备工作——转向
			if index[2] == 'H':
				dir = 'h'
			elif index[2] == 'L':
				dir = 'j'
			sit = armControl.place_ware(dir)				#上下层准备
			time.sleep(1)

			print("进一步动作")
			runControl.runControl(x,y,index[0],index[1])

			print("货物放置动作")
			if index[2] == 'H':
				dir = 'i'
			elif index[2] == 'L':
				dir = 'k'
			sit = armControl.place(dir)						#放置

			runControl.runControl(index[0],index[1],x,y)	#退回一格

			if index[2] == 'H':
				dir = '5'
			elif index[2] == 'L':
				dir = '6'
			sit = armControl.retrive(dir)								#恢复到初始化动作

			currentx = x					#更新路径
			currenty = y

		i += 1								#区分抓和放

		

def good_identify(name):
	identify = {'redsquare':'y','bluesquare':'y','greensquare':'y','yellowsquare':'y',
				'sprite':'y','tennisball':'y','snowflower':'y','badminton':'y',
				'apple':'x',
				'steelwool':'z','sww':'z','yakult':'z'}
	for key in identify:
		if key == name:
			return identify[key]
if __name__ == '__main__':
	planningSite = [(2, 5, 'badminton-2'), (2, 0, 'H'), (4, 2, 'redsquare-1'), (1, 0, 'H'), (4, 2, 'tennisball-2'), (0, 5, 'H'), (2, 5, 'yakult-3'), (0, 0, 'H'), (4, 2, 'sprite-3'), (0, 7, 'H'), (2, 5, 'yellowsquare-1'), (9, 1, 'H'), (7, 4, 'snowflower-2'), (7, 9, 'H'), (5, 7, 'bluesquare-1'), (5, 9, 'H'), (5, 7, 'steelwool-2'), (9, 0, 'H'), (7, 4, 'apple-3'), (4, 9, 'H'), (5, 7, 'sww-3'), (9, 0, 'L'), (7, 4, 'greensquare-1'), (0, 9, 'H')]

	grabPlace(planningSite)				
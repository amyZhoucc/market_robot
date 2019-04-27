import os
for root, dirs, files in os.walk("./image/image_wares"):
		for file in files:
			# # print("str = " + str(os.path.join(root, file)))
			img_dir = str(os.path.join(root, file))
			# str1 = iamg_dir.split('\\')
			print(img_dir)
			# print(str1[1])
dic = []
for i in range(0,10):
	d = {
		'img':i,
		'area':'hello'
		}
	dic.append(d)
print(dic)
list = []
dic1 = {(4,7):'a'}
dic2 = {(5,6):'c'}
list.append(dic1)
list.append(dic2)
print(list)
good_Dir = {(7, 4): [('d', 'green square-1'), ('c', 'snow flower-2'), ('c', 'apple-3')], (4, 2): [('a', 'red quare-1'), ('d', 'tennis ball-2'), ('d', 'sprite-3')], (2, 5): [('b', 'yellow square-1'), ('a', 'badminton-2'), ('a', 'yakult-3')], (5, 7): [('c', 'blue square-1'), ('b', 'steel wool-2'), ('b', 'sww-3')]}
# print(good_Dir[(7,4)][1][0])
good_Dir = {(7, 4): [{'d': 'green square-1'}, {'c': 'snow flower-2'}, {'c': 'apple-3'}], (4, 2): [{'a': 'red quare-1'}, {'d': 'tennis ball-2'}, {'d': 'sprite-3'}], (2, 5): [{'b': 'yellow square-1'}, {'a': 'badminton-2'}, {'a': 'yakult-3'}], (5, 7): [{'c': 'blue square-1'}, {'b': 'steel wool-2'}, {'b': 'sww-3'}]}
# for i in good_Dir[(7,4)]:
# 	for key in i:
# 		print(i[key])
# 	for key in i:
# 		print(key)
#print(good_Dir[(7,4)][1])
dir = {'d':'grenn square-1'}
for key in dir:
	print(dir[key])
good_Dir[(7,4)].remove({'d':'green square-1'})
print(good_Dir[(7,4)])

ware_Dir = {'c': [((7, 9), 'H'), ((5, 9), 'H'), ((4, 9), 'H')], 'a': [((0, 0), 'H'), ((1, 0), 'H'), ((2, 0), 'H')], 'b': [((9, 0), 'H'), ((9, 0), 'L'), ((9, 1), 'H')], 'd': [((0, 7), 'H'), ((0, 5), 'H'), ((0, 9), 'H')]}
for ware in ware_Dir['c']:
	print(ware[1])
	templen_Ware = lib.display_string(ware[0][0][0],ware[0][0][1],currentx,currenty)
good_Dir = {(7, 4): [{'d': 'green square-1'}, {'c': 'snow flower-2'}, {'c': 'apple-3'}], 
			(4, 2): [{'a': 'red quare-1'}, {'d': 'tennis ball-2'}, {'d': 'sprite-3'}], 
			(2, 5): [{'b': 'yellow square-1'}, {'a': 'badminton-2'}, {'a': 'yakult-3'}], 
			(5, 7): [{'c': 'blue square-1'}, {'b': 'steel wool-2'}, {'b': 'sww-3'}]}
for key in good_Dir:
	print(key)
identify = {'redsquare':'r','apple':'a','tennisball':'t','sprite':'x','bluesquare':'b','steelwool':'s','greensquare':'g','sww':'w','snowflower':'h','yellowsquare':'y','yakult':'l','badminton':'m'}
for key in identify:
		if key == 'tennisball':
			print(identify[key])

list = ['b','a','a']
if 'd' in list:
	print(list.index('d'))
elif 'a' in list:
	print(list.index('a'))
elif 'c' in list:
	print(list.index('c'))
elif 'd' in list:
	print(list.index('b'))


import threading
import time
def my_thread1():
        for i in range(0,4):
                print("\n this is a sub thread1")
                time.sleep(1)
def my_thread2():
        for i in range(0,10):
                print("\n this is a sub thread2")
                time.sleep(1)

thread1 = threading.Thread(target = my_thread1,args = ())
thread2 = threading.Thread(target = my_thread2,args = ())
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("\n thread end！")



import retrain_test
import scanStore
import multiprocessing as mp
import time

if __name__ == '__main__':
	p1 = mp.Process(target = retrain_test.label_images,args=())
	p2 = mp.Process(target = scanStore.scanStore,args=())

	p1.start()
	p2.start()
	print(p1)
	print(p2)

import json

str = '{"params":1,"nodename":"topic"}'

params = eval(str)

print(params['params'])

d = {"apple":{'1-1':0.97,'4-3':70.5,'2-3':10.5}
sorted(d.items(),key = lambda x:x[1],reverse = True)
print(d)

L=[{'status':1,'com':'a'},{'status':2 ,'com':'c' },{'status':1 ,'com':'b' },{'status':1 ,'com':'a' }]
L.sort(key=lambda x:(-x['status'],x['com'])) #
print(L)

# list = [('1-1', 0.99992454), ('1-2', 0.03076271), ('4-1', 0.0010711167), ('3-2', 0.00063139887), ('2-1', 0.00043544962), ('4-2', 0.00030311002), ('4-3', 0.00027840401), ('3-3', 0.00019330526), ('3-1', 9.47097e-05), ('1-3', 8.7998218e-05), ('2-2', 1.7776836e-05), ('2-3', 1.4647429e-05)]
img = "4-2"
img+'list' = []
(img+'list').append(4)
print((img+'list'))
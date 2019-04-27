# import os
# for root, dirs, files in os.walk("./image/image_wares"):
# 		for file in files:
# 			# # print("str = " + str(os.path.join(root, file)))
# 			img_dir = str(os.path.join(root, file))
# 			# str1 = iamg_dir.split('\\')
# 			print(img_dir)
# 			# print(str1[1])
dic = []
for i in range(0,10):
	d = {
		'img':i,
		'area':'hello'
		}
	dic.append(d)
print(dic)

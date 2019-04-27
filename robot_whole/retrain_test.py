#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ import print_function

import tensorflow as tf
import sys
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# def label_images():
#     images = os.listdir('test_images')
#     results = {}
#     final_results = {}

#     # Loads label file, strips off carriage return
#     label_lines = [line.rstrip() for line in
#                    tf.gfile.GFile('output_labels.txt')]

#     # Initial the results
#     for line in label_lines:
#         results[line] = ('no', 0)

#     # Unpersists graph from file
#     with tf.gfile.FastGFile('output_graph.pb', 'rb') as f:
#         graph_def = tf.GraphDef()
#         graph_def.ParseFromString(f.read())
#         _ = tf.import_graph_def(graph_def, name='')

#     # Open a session to label images
#     with tf.Session() as sess:
#         for image in images:
#             print(image)
#             softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
#             image_data = tf.gfile.FastGFile(str('test_images/' +
#                                                 image), 'rb').read()
#             predictions = sess.run(softmax_tensor,
#                                    {'DecodeJpeg/contents:0': image_data})
#             top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

#             node_id = top_k[0]
#             human_string = label_lines[node_id]
#             score = predictions[0][node_id]
#             print(image.strip('.jpg'), ': %s  %.5f' % (human_string, score))

#             if score > results[human_string][1]:
#                 results[human_string] = (image.strip('.jpg'), score)

#     for obj, result in results.items():
#         final_results[result[0]] = obj

#     if final_results.get('no'):
#         final_results.pop('no')

#     return final_results


# if __name__ == '__main__':
#     label_images()

import tensorflow as tf
import numpy as np
import os
import time
model_dir = ''
model_name = 'output_graph.pb'
image_dir = 'image/image_goods/separate_goods'
label_dir = ''
label_filename = 'output_labels.txt'


score_whole = {"1-1":[],"1-2":[],"1-3":[],
               "2-1":[],"2-2":[],"2-3":[],
               "3-1":[],"3-2":[],"3-3":[],
               "4-1":[],"4-2":[],"4-3":[]}
tf_result = {}
def use_file(inf):
    res = 'res.bat'
    fileHandle = open ( res, 'w' )
    fileHandle.write (inf)
    # fileHandle.write('\n')
    fileHandle.close()    

def good_define():
    flag ={"apple":False,"badminton":False,"bluesquare":False,"greensquare":False,"redsquare":False,
           "snowflower":False,"sprite":False,"steelwool":False,"sww":False,"tennisball":False,"yakult":False,
            "yellowsquare":False}
    highest_score = []      #将照片中当前最高的评分放进列表
    for key in score_whole:
        highest_score.append((key,score_whole[key][0][0],score_whole[key][0][1]))
    print(highest_score)
    while len(highest_score) != 0:
        time.sleep(1)
        highest_score.sort(key=lambda x:x[2],reverse=True)
        # print(highest_score)
        if flag[highest_score[0][1]] == False:
            flag[highest_score[0][1]] = True
            tf_result[highest_score[0][0]] = highest_score[0][1]
            highest_score.remove(highest_score[0])
            print(highest_score)
        else:
            # print(score_whole[highest_score[0][0][0])
            score_whole[highest_score[0][0]].remove(score_whole[highest_score[0][0]][0])
            highest_score.append((highest_score[0][0],score_whole[highest_score[0][0]][0][0],score_whole[highest_score[0][0]][0][1]))
            highest_score.remove(highest_score[0])
    use_file(str(tf_result))

    # print(highest_score)



# 读取并创建一个图graph来存放Google训练好的Inception_v3模型（函数）
def create_graph():
    with tf.gfile.FastGFile(os.path.join(
            model_dir, model_name), 'rb') as f:
        # 使用tf.GraphDef()定义一个空的Graph
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        # Imports the graph from graph_def into the current default Graph.
        tf.import_graph_def(graph_def, name='')

# 读取标签labels
def load_labels(label_file_dir):
    if not tf.gfile.Exists(label_file_dir):
        # 预先检测地址是否存在
        tf.logging.fatal('File does not exist %s', label_file_dir)
    else:
        # 读取所有的标签返并回一个list
        labels = tf.gfile.GFile(label_file_dir).readlines()
        for i in range(len(labels)):
            labels[i] = labels[i].strip('\n')
    return labels

# 创建graph

def label_images():
    create_graph()
    outcome = {}            #最后结果输出为一个字典
    # 创建会话，因为是从已有的Inception_v3模型中恢复，所以无需初始化
    with tf.Session() as sess:
        # Inception_v3模型的最后一层final_result:0的输出
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        # 遍历目录
        for root, dirs, files in os.walk(image_dir):
            # print(files)
            for file in files:
                judge = file.split(".")
                if(judge[1] != 'jpg'):
                    continue
                print(file)
                # 载入图片
                image_data = tf.gfile.FastGFile(os.path.join(root, file), 'rb').read()
                # 输入图像（jpg格式）数据，得到softmax概率值（一个shape=(1,1008)的向量）
                predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
                # 将结果转为1维数据
                predictions = np.squeeze(predictions)
        
                # 打印图片路径及名称
                image_path = os.path.join(root, file)
                # print(image_path)
                # good_name = (image_path.split('\\')[1]).split('.')[0]
                good_name = (image_path.split('/')[3]).split('.')[0]
                print(good_name)
                
                # 排序，取出前5个概率最大的值（top-5),本数据集一共就5个
                # argsort()返回的是数组值从小到大排列所对应的索引值
                top_12 = predictions.argsort()[-12:][::-1]
                # print(top_12)
                for label_index in top_12:
                    # 获取分类名称
                    label_name = load_labels(os.path.join(
                            label_dir, label_filename))[label_index]
                    # 获取该分类的置信度
                    label_score = predictions[label_index]
                    print('%s (score = %.5f)' % (label_name, label_score))
                    # dir = {good_name:label_name}
                    # print(dir)
                    # outcome[good_name] = label_name
                    score_whole[good_name].append((label_name,label_score))
                # print()
        # use_file(str(outcome))
        
        good_define()

if __name__ == '__main__':
    label_images()
    # use_file()


#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from sklearn import decomposition, ensemble

import pandas, xgboost, numpy, textblob, string

from keras.preprocessing import text, sequence

from keras import layers, models, optimizers

level1 = (     (1,1,1,1,1,1),
     (1,0,0,0,0,1),
     (1,0,0,0,0,1),
     (1,0,0,0,0,1),
     (1,0,0,0,0,1),
     (1,1,1,1,1,1))

list1 = ('runoob', 786 , 2.23, 'john', 70.2 )
tinylist = [123, 'john']
#list(0)='test1'
#print list # 输出完整列表

tuple = (1,2,3)
print "First: %d, Second: %d, Third: %d" % tuple

print level1

#tmp = [list(row1) for row1 in level1]

level1 = map(list,level1)
print list(level1)



#print list1[1] # 输出列表的第一个元素
#print list1[0:1] # 输出第二个至第三个元素
#print list1[2:] # 输出从第三个开始至列表末尾的所有元素
#print tinylist * 2 # 输出列表两次
#print type(list1)


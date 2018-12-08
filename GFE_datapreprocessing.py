# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:37:44 2018

@author: Helena J Arpudaraj
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#read the data files
x_b1 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_conditional_datapoints.txt',sep = " ")
y_b1 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_conditional_targets.txt', sep = " ")

x_b2 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_emphasis_datapoints.txt',sep = " ")
y_b2 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_emphasis_targets.txt', sep = " ")

x_b3 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_affirmative_datapoints.txt',sep = " ")
y_b3 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_affirmative_targets.txt', sep = " ")

x_b4 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_yn_question_datapoints.txt',sep = " ")
y_b4 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_yn_question_targets.txt', sep = " ")

x_b5 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_wh_question_datapoints.txt',sep = " ")
y_b5 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_wh_question_targets.txt', sep = " ")

x_b6 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_topics_datapoints.txt',sep = " ")
y_b6 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_topics_targets.txt', sep = " ")

x_b7 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_relative_datapoints.txt',sep = " ")
y_b7 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_relative_targets.txt', sep = " ")

x_b8 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_negative_datapoints.txt',sep = " ")
y_b8 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_negative_targets.txt', sep = " ")

x_b9 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_doubt_question_datapoints.txt',sep = " ")
y_b9 = pd.read_csv('C:/Users/Helena J Arpudaraj/Desktop/grammatical_facial_expression/b_doubt_question_targets.txt', sep = " ")

fig = plt.figure(figsize = (60,20))
plt.scatter(x_b['26x'],y_b,color = 'red')
plt.scatter(x_b['27x'],y_b+0.1,color = 'green')
plt.scatter(x_b['28x'],y_b+0.2,color = 'orange')
plt.scatter(x_b['29x'],y_b+0.3,color = 'pink')
plt.scatter(x_b['30x'],y_b+0.4,color = 'blue')
plt.show()

list2 = ['affirmative_datapoints',
'conditional_datapoints',
'yn_question_datapoints',
'wh_question_datapoints',
'topics_datapoints',
'relative_datapoints',
'negative_datapoints',
'emphasis_datapoints',
'doubt_question_datapoints']

list1 = [x_b1,x_b2,x_b3,x_b4,x_b5,x_b6,x_b7,x_b8,x_b9]
j = 0
for i in list1:
    x = i['87x']
    y = i['88x']
    print(list2[j]+ "\t\t")
    print("--------------------")
    print("\n")
    print(np.corrcoef(x,y))
    print("\n")
    j = j+1
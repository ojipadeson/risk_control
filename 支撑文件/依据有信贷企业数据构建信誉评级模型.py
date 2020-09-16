# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:12:01 2020

@author: MI
"""
import pydotplus
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from IPython.display import Image
from sklearn import tree
import joblib
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

data = pd.read_csv('label123.csv',index_col = 0).reset_index(drop=True)

x = data.iloc[:,[0,1,2,14]]
# 如果用全部数据直接构成决策树，注释掉上一行，使用下一行
# x = data.drop(columns = ['level'])
y = data.loc[:,'level']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=19768)

# 下面3行分别为回归树，随机森林，和决策树，且都已剪枝
# 如果需要未剪枝的模型则 min_samples_leaf=1
# tree_classifier = DecisionTreeRegressor(criterion="mse",min_samples_leaf = 10,random_state=1).fit(X_train,y_train)
# tree_classifier = RandomForestClassifier(min_samples_leaf = 10,random_state=123).fit(X_train,y_train)
tree_classifier = DecisionTreeClassifier(criterion="entropy",min_samples_leaf = 10,random_state=123).fit(X_train,y_train)

joblib.dump(tree_classifier, 'tree123.pkl')

def print_tree(model, x):
    dot_data = \
    tree.export_graphviz(
        model,
        out_file=None,
        feature_names=x.columns[:],  #特征名字
        filled=True,
        impurity=False,
        rounded=True
    )
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.get_nodes()[7].set_fillcolor("#FFF2DD")
    Image(graph.create_png())
    graph.write_png("tree.png")
    return

# 如果使用随机森林则将下一行注释掉
print_tree(tree_classifier, X_train)

# 如果需要判断训练集的拟合程度则将X_test换成X_train
tree_pred = tree_classifier.predict_proba(X_test)

def top_2(array):
    top_list = []
    top_list.append(array.argmax()+1)
    # 如果需要top1准确率数据则将下面三行注释掉
    if array[array.argmax()] != 1:
        array[array.argmax()] = 0
        top_list.append(array.argmax()+1)
    return top_list

tree_accuracy = 0
# 如果判断训练集的拟合程度取消下一行的注释
# y_test = y_train
for i in range(len(y_test)):
    if y_test.iloc[i] in top_2(tree_pred[i]):
        tree_accuracy += 1
    # 如果使用回归树则注释掉上面两行，将下面一段取消注释
    # if (y_test.iloc[i] == 100 and tree_pred[i] > 90) or \
    #     (y_test.iloc[i] == 80 and 70 < tree_pred[i] <= 90) or \
    #     (y_test.iloc[i] == 60 and 50 < tree_pred[i] <= 70) or \
    #     (y_test.iloc[i] == 0 and tree_pred[i] <= 50):
    #     tree_accuracy += 1
tree_accuracy = tree_accuracy / len(y_test)

print(tree_accuracy)

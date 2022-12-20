# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:46:40 2022

@author: Eason Chen
"""

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

train = pd.read_csv("train.csv",encoding="utf-8")
print(train)
# -*- coding:utf-8 -*-
import csv

# 日本の名称リストを取得する
def get_list():
    with open('./parms/japna-cities.csv', 'r') as f:
        reader = list(csv.reader(f))
        return reader
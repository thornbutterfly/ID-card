#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import random
import datetime
from pathlib import Path
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# DC_PATH = BASE_DIR + "districtcode.txt"
本地路径 = Path(__file__)
上一级 = Path(__file__).parent
'''
print(上一级 / 'districtcode.txt')
file = open(上一级 / 'districtcode.txt', 'r', encoding='UTF-8', errors='ignore')
read = file.read()
print(read)
'''


def getdistrictcode():
    # districtcode.txt 需要放在同一目录下
    with open(上一级 / 'districtcode.txt', 'r', encoding='UTF-8', errors='ignore') as file:
        data = file.read()
        districtlist = data.split('\n')
    for node in districtlist:
        # print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' 'and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' 'and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city,
                             "district": district, "code": code})


def gennerator():
    global codelist
    codelist = []
    if not codelist:
        getdistrictcode()
    id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
    id = id + str(random.randint(1930, 2013))  # 年份项
    da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8',
                 '5': '7', '6': '6', '7': '5', '8': '5', '9': '3', '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id

for x in range(10):
    print(gennerator())

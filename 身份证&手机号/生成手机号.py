#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


# def create_num():
#     list = ['135', '156', '155', '189']
#     str = '0123456789'
#     for i in range(500):
#         print(random.choice(list) + "".join(random.choice(str)
#                                             for i in range(8)))
# create_num()


def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147",
               "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    print(random.choice(prelist) + "".join(random.choice("0123456789")
                                           for i in range(8)))
for i in range(100):
    createPhone()

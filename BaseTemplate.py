# -*- coding: utf-8 -*-#

import sys

# Name:         
# Description:
# Author:       gongzhao
# Date:         2020/9/19

def getitem(title,subtitle):
    if title:
        item = {}
        item['title'] = title
        item['subtitle'] = subtitle
        item['icon'] = geticon()
        item['arg'] = title
        return item

    else:
        return None

def geticon():
    icon = {}
    icon['path'] = 'icon.png'
    return icon

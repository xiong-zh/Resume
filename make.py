#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
# FileName: make.py
# Desc: 使用jiaja2从yal读取信息生成静态页面
# Author: zhangxiong
# Email: imzhangxiong@gmail.com
# HomePage: www.zhangxiong.net
# Version: 7.0.0
# Created: 2020/6/5 下午9:51
#=============================================================================
"""

import os
import json

import yaml
from jinja2 import Template

ROOT = os.path.dirname(os.path.abspath(__file__))

base_html = os.path.join(ROOT, 'base.html')

yaml_file = os.path.join(ROOT, 'me.yml')

index_html = os.path.join(ROOT, 'index.html')

if __name__ == '__main__':
    with open(yaml_file, 'r') as yml:
        dic = yaml.safe_load(yml)

    with open(base_html, 'rt') as base:
        source = base.read()

    template = Template(source, autoescape=False)
    html = template.render(**dic)

    with open(index_html, 'wt') as index:
        index.write(html)

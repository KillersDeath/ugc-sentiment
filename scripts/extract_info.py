# -*- coding:utf-8 -*-
"""
Extract information
@version: 1.0
@author: kevin
@license: Apache Licence
@contact: liujiezhang@bupt.edu.cn
@site:
@software: Atom
@file: extract_info.py
@time: 17/7/8 下午12:31
"""
import re
import sys
from collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    datas = open('../docs/shenyang_topic.txt', 'r').readlines()
    topic_pattern = re.compile('宗教')
    topic_data = filter(lambda cont: re.search(topic_pattern, cont), datas)
    time_data = defaultdict(list)
    for line in topic_data:
        day = re.search('(\d{4}\-\d{2}\-\d{2})', line.split('|@|')[-2]).group(0)
        time_data[day].append(line)
    for key in time_data:
        print('%s : %d' % (key, len(time_data[key])))

# -*- coding: utf-8 -*-
import json
import re

import neologdn

re_and = re.compile(' &[ !]')
PATH = 'pn.csv.m3.120408.trim'
with open(PATH) as fd:
    word_dict = {}
    for line in fd:
        word, polarity, word_type = line.split('\t')
        if polarity == 'e':
            continue
        word = neologdn.normalize(word)
        word_dict.update({word: polarity})
    json.dump(word_dict, open('pn_noun.json', 'w'))


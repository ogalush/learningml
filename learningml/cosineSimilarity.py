#!/usr/bin/env python3
# vim:fileencoding=utf-8
# coding=utf8
'''
Created on 2019/05/26
@author: ogalush
'''

# コサイン類似度を求めるスクリプト
# 10 対 10のストレングスファインダーの属性順位同士を比較させる.
# 参考
# 【Python】コサイン類似度
# https://qiita.com/Qiitaman/items/fa393d93ce8e61a857b1
# 実行例
# ----
# Macbook1:learningml ogalush$ python3 cosineSimilarity.py 
# bengoshi0 bengoshi0 1.0
# bengoshi0 bengoshi1 0.7351
# bengoshi0 bengoshi2 0.8155
# ...(略)...
# ----

# モジュールのimport
import numpy as np
import json

# コサイン類似度計算
def cos_sim(v1, v2):
    return round(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), 4)

# MAIN
# JSON読込み
json_file = open('/Users/ogalush/git/learningml/learningml/bengoshi.json', 'r')
json_obj  = json.load(json_file)

#　値の取得
for i in range(0, 9, 1):
  XHash = json_obj['bengoshi' + str(i)]
  XList = XHash.values()
  for j in range(0, 9, 1):
    YHash = json_obj['bengoshi' + str(j)]
    YList = YHash.values()

    # コサイン類似度の計算と結果出力
    print ('bengoshi' + str(i) + ' ' + 'bengoshi' + str(j) + ' ' + str(cos_sim(list(XList), list(YList))))

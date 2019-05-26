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

# モジュールのimport
import numpy as np
import json
# コサイン類似度計算
def cos_sim(v1, v2):
    return round(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)), 4)
# MAIN
# ファイルを開く
json_file = open('/Users/ogalush/git/learningml/learningml/bengoshi.json', 'r')

# JSONを読み込み
json_obj  = json.load(json_file)

#　値の取り出し
for i in range(0, 9, 1):
  XHash = json_obj['bengoshi' + str(i)]
  XList = XHash.values()
  for j in range(0, 9, 1):
    YHash = json_obj['bengoshi' + str(j)]
    YList = YHash.values()

    # 計算結果出力
    print ('bengoshi' + str(i) + ' ' + 'bengoshi' + str(j) + ' ' + str(cos_sim(list(XList), list(YList))))
    #print(cos_sim(list(XList), list(YList))) 

#!/usr/bin/env python3
# coding=utf-8
'''
Created on 2019/04/06
@author: ogalush
'''
import random

class strengthsFinder():
    ## Strengthファインダー属性を取得する
    def getStrengthDict(self):
        strangthDict = {
            'ポジティブ' : 0,
            '個別化' : 0,
            '活発性' : 0,
            'アレンジ' : 0,
            '最上志向' : 0,
            '着想' : 0,
            '運命思考' : 0,
            '社交性' : 0,
            '調和性' : 0,
            '共感性' : 0,
            '包含' : 0,
            '成長促進' : 0,
            '達成欲' : 0,
            'コミュニケーション' : 0,
            '適応性' : 0,
            '原点思考' : 0,
            '内省' : 0,
            '未来志向' : 0,
            '学習欲' : 0,
            '戦略性' : 0,
            '親密性' : 0,
            '自己確信' : 0,
            '責任感' : 0,
            '指令性' : 0,
            '競争性' : 0,
            '収集心' : 0,
            '公平性' : 0,
            '分析思考' : 0,
            '回復志向' : 0,
            '自我' : 0,
            '目標志向' : 0,
            '信念' : 0,
            '規律性' : 0,
            '慎重さ' : 0,
        }
        return strangthDict


    ## ランキング用数字を埋め込み
    def setStrangthValue(self, strangthDict):
        ## ランキング用の数字を取得
        rankList = list(range(len(strangthDict)))
        random.shuffle(rankList)
        ## 各ストレングスへ埋め込み
        i = 0
        for strength in strangthDict:
            strangthDict[strength] = rankList[i]
            i+=1
        return strangthDict

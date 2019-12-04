# -*- coding:utf-8 -*-
from polyglot.text import Text
import cities

# 日本が含まれているか確認する
def match_japan(tags):
    isMatch = False
    for token in tags:
        if token[0] == "Japan" and token[1] == "PROPN":
            isMatch = True
    return isMatch

# 日本の都市名が含まれているか確認する
def match_city(tokens, cities):
    # 初期返却値はNone
    result = None
    for token in tokens:
        # 固有名詞のときだけ処理する
        if token[1] == "PROPN":
            for city in cities:
                print(city[0])
                if city[0] == token[0]:
                    result = city[1]
    return result

# 形態素解析を行います
def morphological(text):
    tokens = Text(text)
    return tokens.pos_tags
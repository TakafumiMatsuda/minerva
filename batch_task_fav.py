# import schedule
# import time
# import datetime
from twitter_favorite_automated import favorite_automated


def batch_task1():
    print("batck task1 実行")
    favorite_automated(words1, favs1)

def batch_task2():
    print("batck task2 実行")
    favorite_automated(words2, favs2)


# ふぁぼ条件決定
words1 = ['"ロジカルシンキング"', '"科学的思考"', '"科学的手法"', '"サイエンスコミュニケーター"', "研究者志望"', '"院試"', '"ポスドク"']
words2 = ['"フラーレン"', '"有機化学合成"', '"アーク放電法"', '"アルゴンガス"', '"コランニュレン"', '"ベンゼン環"']
favs1 = 10
favs2 = 5

# 実行
batch_task1()
batch_task2()
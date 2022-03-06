# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re

def solution(N):
    # write your code in Python 3.6

    # 受け取った変数を二進数に変換
    N = format(N, 'b')

    # 0が1で囲まれた文字列を配列に格納
    # N = 529のときは'1000010001'なので
    # ['00001', '0001']
    r = re.findall('0+1', N)

    max_zero = 0
    for n in range(len(r)):
        # 配列の要素の'0'の個数と直近の'0'の個数を比較
        if r[n].count('0') > max_zero:
            max_zero = r[n].count('0')
        else:
            pass

    return max_zero
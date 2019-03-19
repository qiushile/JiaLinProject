# -*- coding: utf-8 -*-
__author__ = "lance"
import re

def getDigiStr(file_path):
    fp = open(file_path, 'r')
    file_text = fp.read()
    digi_str = re.findall(r'([0-9]+)',file_text,re.MULTILINE)
    fp.close()
    #数字
    return '\n'.join(digi_str)


def getLetterStr(file_path):
    fp = open(file_path, 'r')
    file_text = fp.read()
    letter_str = re.findall(r'([a-zA-Z]+)',file_text,re.MULTILINE)
    fp.close()
    #字母
    return ''.join(letter_str)

if __name__ == '__main__':
    print(getDigiStr(r'/Users/lance/Desktop/For嘉琳/深证股票代码一览表.txt'))

    # print(getLetterStr(r'test.txt'))
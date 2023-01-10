import telebot
import random

def rle_code(data):
    coding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                coding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
                count += 1
    else:
        coding += str(count) + prev_char
        return coding
    
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

def znak_har():
    dict = {}
    with open('D:\УЧЕБА\PYTON\DZ\DZ_2212\har.txt', 'r', encoding='utf-8') as file:
        for i in range(12):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
    return dict


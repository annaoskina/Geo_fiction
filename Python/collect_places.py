from fugashi import Tagger
import os
import re
from collections import Counter
import csv,sys

def read_file(path, filename):
	file = open('{}/{}'.format(path, filename), 'r', encoding = 'utf-8')
	text = file.read()
	text_without_rubi = re.sub('《.+?》', '', text)
	file.close()
	return text_without_rubi

def extract_places(text, tagger):
    tagger.parse(text)
    list_places = []
    for word in tagger(text):
        if word.feature.pos3 == '地名':
            #print(word, word.feature, '\n')
            list_places.append(word.surface)
    return list_places

def normalize_place(place):
    normalized_dict = {'露西亞': 'ロシア', '亜': 'アメリカ', '魯西亜': 'ロシア', '清': '中国', '清国': '中国', '江戸': '東京', '大和 ': '日本', '欧州' : 'ヨーロッパ', 'Europe' : 'ヨーロッパ', '欧羅巴' : 'ヨーロッパ', '欧洲' : 'ヨーロッパ', '露西亜': 'ロシア', '露国': 'ロシア', 'Russia': 'ロシア', '亜米利加': 'アメリカ', '米国': 'アメリカ', 'America': 'アメリカ', '支那': '中国', 'China': '中国', '唐': '中国', 'シナ': '中国', '英国': 'イギリス', '印度': 'インド', '仏蘭西': 'フランス', 'France': 'フランス', '仏国': 'フランス', '巴里': 'パリ', 'Paris': 'パリ', '独逸': 'ドイツ', '德国': 'ドイツ', 'Germany': 'ドイツ', '倫敦': 'ロンドン', 'London': 'ロンドン', '伯林': 'ベルリン', 'Berlin': 'ベルリン', '伊太利亜': 'イタリア', 'イタリイ': 'イタリア', 'イタリー': 'イタリア', 'ベニス':'ヴェネチア', 'ヴェニス':'ヴェネチア', 'ヴェニース':'ヴェネチア'}
    try:
        return normalized_dict[place]
    except:
        return place 

def count_places_add_coordinates(list_places, list_places_with_coordinates):
    places_in_file = []
    for word, frequency in Counter(list_places).most_common():
        for place in list_places_with_coordinates:
            if word == place[0]:
                places_in_file.append(word + ',' + str(frequency) + ',' + place[2] + ',' + place[3])
    return places_in_file    #France, 4, lat, lon\n

def extract_data(name_csv):
    with open(name_csv, encoding = 'utf-8') as r_file:
        data = csv.reader(r_file, delimiter = ',')
        data_list = list(data)
        #print(data_list)
    return data_list

path = '/home/annaoskina/HSE_master/DigitalOrientalist/Geo_fiction/Data'
files = os.listdir(path)
result_places = []
x = 1
tagger = Tagger('-Owakati')
result_tally = ['filename,title_jp,author,place_name,frequency,lat,lon\n']

name_csv = 'places_with_coordinates_shortlist.csv'
places_coord = extract_data(name_csv)

for filename in files:
    try:
        text = read_file(path, filename)
        print(filename)
        meta_data = filename.strip('.txt') + ',' + text.split('\n')[0] + ',' + text.split('\n')[1] #here we add to filename title and author
        list_places = extract_places(text, tagger)
        clean_list_places = []
        for place in list_places:
            clean_list_places.append(normalize_place(place))
        places_in_file = count_places_add_coordinates(clean_list_places, places_coord) 
        for place in places_in_file:
            data = meta_data +','+ place + '\n'
            result_tally.append(data)
        x += 1
    except UnicodeDecodeError:
        print('UnicodeDecodeError:', filename)

with open('result_tally.csv', 'w', newline = '\n', encoding = 'utf-8') as file:
    for row in result_tally:
        file.write(row)

print('Done')

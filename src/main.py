import requests
import openpyxl
from bs4 import BeautifulSoup

import codecs

def crawling_find(web_addr ,tag ,specification):
	#web_addr = https://altema.jp/assaultlily/memorialist
	res = requests.get(web_addr)
	soup = BeautifulSoup(res.content, 'html.parser')
	#tag = 'tr'
	data = soup.find_all(tag)
	mem_list = []
	#specifictaion = 'data-obj'
	for dat in data:
		if dat.get(specification) != None:
			mem_list.append(dat.get(specification))
	return mem_list

def crawling_select(web_addr ,tag ):#, specification):
	#web_addr = https://altema.jp/assaultlily/memorialist
	res = requests.get(web_addr)
	soup = BeautifulSoup(res.content, 'html.parser')
	#tag = 'tr'
	mem_list = []
	data = soup.select(tag)
	#specification = 'alt'
	for dat in data:
		if dat.get_text() != None:
			mem_list.append(dat.get_text())

	return mem_list


def extract(data):
	information = []
	#1. id
	front = data.find('id')
	end = data.find(',')
	information.append(data[front+4:end])
	#2. name
	front = data.find('name')
	end = data.find('",',front)
	information.append(data[front+7:end])
	#3. rare
	front = data.find('rea":')
	end = data.find(',',front)
	information.append(data[front+5:end])
	#zokusei>
	#=> 1: 화속, 2: 수속 3: 풍속
	#memoria_type >
	#=>1. 통상단일공격 2. 통상복수공격 3. 특수단일공격 4. 특수복수공격
	#=>5. 아군 버프 6. 적 디버프 7. 회복
	#4. feature
	front = data.find('zokusei":')
	end = data.find(',',front)
	chk = data[front+9:end]
	#'''
	if chk == '1':
		chk = 'fire'
	elif chk == '2':
		chk = 'water'
	elif chk == '3':
		chk = 'wind'
	else:
		chk = 'unknown'
	#'''
	information.append(chk)
	#5. mem_type
	front = data.find('"memoria_type":')
	end = data.find(',',front)
	chk = data[front+15:end]
	#'''
	if chk == '1':
		chk = 'normal_single_attack'
	elif chk == '2':
		chk = 'normal_multi_attack'
	elif chk == '3':
		chk = 'special_single_attack'
	elif chk == '4':
		chk = 'special_multi_attack'
	elif chk == '5':
		chk = 'buff'
	elif chk == '6':
		chk = 'debuff'
	elif chk == '7':
		chk = 'heal'
	else:
		chk = 'unknown'
	#'''
	information.append(chk)
	#6. status(0: atk, 1: sp_atk, 2: def, 3: sp_atk)
	'''
	status = []
	front = data.find('"atk":')
	end = data.find(',',front)
	status.append(data[front+6:end])
	front = data.find('"sp_atk":')
	end = data.find(',',front)
	status.append(data[front+9:end])
	front = data.find('"def":')
	end = data.find(',',front)
	status.append(data[front+6:end])
	front = data.find('"sp_atk":')
	end = data.find(',',front)
	status.append(data[front+9:end])
	information.append(status)
	'''
	status = []
	front = data.find('"atk":')
	end = data.find(',',front)
	information.append(data[front+6:end])
	front = data.find('"sp_atk":')
	end = data.find(',',front)
	information.append(data[front+9:end])
	front = data.find('"def":')
	end = data.find(',',front)
	information.append(data[front+6:end])
	front = data.find('"sp_atk":')
	end = data.find(',',front)
	information.append(data[front+9:end])
	#information.append(status)
	#7. skill_types(0: huge_type, 1: legion_type, 2: legion_support_type)
	'''
	skills = []	
	front = data.find('"huge_type":')
	end = data.find(',',front)
	skills.append(data[front+12:end])
	front = data.find('"legion_type":')
	end = data.find(',',front)
	skills.append(data[front+14:end])
	front = data.find('"legion_hojo_type":')
	end = data.find('}',front)
	skills.append(data[front+19:end])
	information.append(skills)
	print(information)
	'''

	front = data.find('"huge_type":')
	end = data.find(',',front)
	chk = data[front+12:end]
	#'''
	if chk == '1':
		chk = 'attack'
	elif chk == '2':
		chk = 'heal'
	elif chk == '3':
		chk = 'buff'
	elif chk == '4':
		chk = 'debuff'
	else:
		chk = 'unknown'
	#'''
	information.append(chk)

	front = data.find('"legion_type":')
	end = data.find(',',front)
	chk = data[front+14:end]
	#'''
	if chk == '1':
		chk = 'attack'
	elif chk == '2':
		chk = 'heal'
	elif chk == '3':
		chk = 'buff'
	elif chk == '4':
		chk = 'debuff'
	else:
		chk = 'unknown'
	#'''
	information.append(chk)

	front = data.find('"legion_hojo_type":')
	end = data.find('}',front)
	chk = data[front+19:end]
	#'''
	if chk == '1':
		chk = 'attack'
	elif chk == '2':
		chk = 'heal'
	elif chk == '3':
		chk = 'buff'
	elif chk == '4':
		chk = 'debuff'
	#'''
	information.append(chk)
	return information




#id":200,
#"name":"\u653e\u8ab2\u5f8c\u30d5\u30a1\u30f3\u30bf\u30ba\u30e0",
#"furigana":"\u307b\u3046\u304b\u3054\u3075\u3041\u3093\u305f\u305a\u3080",
#"ichiran_name":"\u653e\u8ab2\u5f8c\u30d5\u30a1\u30f3\u30bf\u30ba\u30e0",
#"chara_name":"","chara_furigana":"",
#"rea":5,"zokusei":1,"memoria_type":2,"hyoka":85,
#"saikyo_rank_id":3,"huge_rank_id":3,"legion_rank_id":4,
#"atk":1970,"sp_atk":1338,"def":1904,"sp_def":1337,
#"huge_type":1,"legion_type":1,"legion_hojo_type":4}
#rea>
#=>rarelity(5성,4성,3성)
#zokusei>
#=> 1: 화속, 2: 수속 3: 풍속
#memoria_type >
#=>1. 통상단일공격 2. 통상복수공격 3. 특수단일공격 4. 특수복수공격
#=>5. 아군 버프 6. 적 디버프 7. 회복
#huge_type>
#legion_type>
#legion_hojo_type>
#name: 메모리아 이름, rea: 별, zokusei: 속성, memoria_type: 메모리얼 타입,
#atk: 일공, sp_atk: 특공, def: 일방, sp_def: 특방
#huge_type: 휴지 스킬, legion_type: 레기온 스킬, legion_hojo_type: 레기온 보조 스킬
#attack : 1, heal : 2, buff = 3, debuff = 4
'''
def translate(information):
	
'''	

def write_excel_template(filename, sheetname_1, listdata_1, sheetname_2, listdata_2):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    excel_sheet_2 = excel_file.create_sheet()

    if sheetname_1 != '':
        excel_sheet.title = sheetname_1
    
    for item in listdata_1:
        excel_sheet.append(item)

    if sheetname_2 != '':
        excel_sheet_2.title = sheetname_2
    
    for item in listdata_2:
        excel_sheet_2.append(item)

    excel_file.save(filename)
    excel_file.close()

def main():
	web_addr = 'https://altema.jp/assaultlily/memorialist'
	tag = 'tr'
	specifictaion = 'data-obj'
	#필요 tag: name, rea, zokusei, memoria_type, atk, sp_atk, def, sp_def
	mem_list = crawling_find(web_addr ,tag ,specifictaion)
	data_list = []
	for memorial in mem_list:
		data_list.append(extract(memorial))

	tag = 'table#result-table > tbody > tr > td > a'
	name_list = []
	name_list = crawling_select(web_addr ,tag)

	n_list = []
	index = 0
	for name in name_list:
		if index % 4 == 0:
			name_list[index] = name_list[index].replace('\n','')
			name_list[index] = name_list[index].replace('\r','')
			name_list[index] = name_list[index].replace(' ','')
			n_list.append(name_list[index])
		index = index + 1

	# print(n_list)
	print(len(n_list))
	print(len(data_list))

	for i, memorial in enumerate(data_list):
		print(memorial)
		if i == len(n_list):
			break
		data_list[i][1] = n_list[i]
		print(data_list[i])

	features = ["ID","NAME","RARE","FEATURE","TYPE","ATK","SP_ATK","DEF","SP_DEF","HUGE_SKILL","LEGION_SKILL","LEGION_SUPPORT_SKILL"]	
	data_list.insert(0,features)
	# for memorial in data_list:
	# 	print(memorial)
	web_addr_1 = 'https://gamerch.com/assaultlily/entry/218328'
	tag_1 = 'div.mu__closebox--contents > div.mu__closebox--wrap > h2'
	list_1 = crawling_select(web_addr_1 ,tag_1)
	tag_2 = 'div.mu__closebox--contents > div.mu__closebox--wrap > div.mu__table > table > tbody > tr > td'
	list_2 = crawling_select(web_addr_1 ,tag_2)


	update_list = []
	normal = []
	ticket = []

	for n in list_1:
		chk = n.find('チケットガチャ')
		if(chk != -1):
			ticket.append(n)
		else:
			normal.append(n)

	for n in list_2:
		if n[:3] == '202':
			update_list.append(n[:10])
	
	gacha_list = [['가챠 이름','개최 일시']]
	for i in range(len(update_list)):
		temp = []
		temp.append(normal[i])
		temp.append(update_list[i])
		gacha_list.append(temp)

	for element in gacha_list:
		print(element)
	
	write_excel_template('lily.xlsx','memoria', data_list, 'gacha', gacha_list)

if __name__ == "__main__":
	main()
	
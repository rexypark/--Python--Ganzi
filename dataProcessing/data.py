# -*- coding: utf-8 -*-
#https://www.thefc.co.kr:4431/pknu
import json
from pandas import DataFrame
import pandas as pd


all_data = open('/Users/rexypark/spyder_py/FinalProject/all_data.txt','r')

data = all_data.read()
#문자열을 벋겨주는 json
data_list = json.loads(data)


df_data = pd.DataFrame(data_list)
print(df_data)
#생일로 내림차순 정렬
sort_data = df_data.sort_values(by='birth')
print(len(sort_data))

one = sort_data.loc[sort_data['user_id'].isin([1])]
print(one)

persnal_data = []
for i in range(0,168):
    if 0 != sort_data.loc[sort_data['user_id'].isin([i])].size:
        persnal_data.append(sort_data.loc[sort_data['user_id'].isin([i])])




for i in range(0,len(persnal_data)):
                             # [행번호,컬럼번호]
    user_id = persnal_data[i].iloc[0,10]
    
    # 각각의 아이디값을 하나씩 꺼내 10번째 컬럼(user_id)의
    # 0번째 행값을 출력하여 해당아이디를 순서에 맞는 번호로 id를 바꿔준다.
    persnal_data[i]['user_id'].replace(
            to_replace=[user_id],
            value=i+1,
            inplace=True)
    persnal_data[i].columns = ["잔고", "생년월일","주소", "입출내역", "거래내역","성별","금액","날짜","시간","거래유형","user_id"]    
    persnal_data[i].index= range(len(persnal_data[i].index))

#persnal_data리스트에 각 인덱스에 한명의 총 거래량이 들어있음
#persnal_data > DataFrame
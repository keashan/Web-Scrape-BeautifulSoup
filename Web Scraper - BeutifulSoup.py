import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

rows=soup.find_all('tr')
list_rows=[]
for row in rows:
    row_td=row.find_all('td')
    cleantext=BeautifulSoup(str(row_td),"html.parser").get_text()
    cleantext.replace('\r','').replace('\n','')
    list_rows.append(cleantext)
df=pd.DataFrame(list_rows)

col_labels=soup.find_all('th')
all_header=[]
col_str=str(col_labels)
cleantext2=BeautifulSoup(col_str,"html.parser").get_text()
all_header.append(cleantext2)

df2=pd.DataFrame(all_header)

df4=pd.concat([df2,df])

df4[0]=df4[0].str.strip('[')
df4[0]=df4[0].str.strip(']')

df1=df4[0].str.split(',',expand=True)

df1.head()

df5=df1.rename(columns=df1.iloc[0])
df5.head()

df6=df5.dropna(axis=0,how='any')
df6.drop(df6.index[0],inplace=True)
df6.replace(r'\s', '', regex = True, inplace = True)
df6.head()
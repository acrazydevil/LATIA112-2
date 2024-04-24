# 引入所需的庫
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 設置目標網站的URL
url = 'https://sai083.pixnet.net/blog'

# 使用requests發出HTTP GET請求到指定URL
response = requests.get(url)
# 設定響應內容的編碼，確保中文顯示正確
response.encoding = 'utf-8'

# 使用BeautifulSoup解析網頁的HTML內容
soup = BeautifulSoup(response.text, 'lxml')

# 初始化一個空的list來儲存文章信息
article = []

# 尋找所有的<div>標籤並過濾出class為'article'的div標籤
for articles in soup.find_all('div', class_='article'):
    # 提取文章的標題，位於class為'title'的<li>標籤內
    title = articles.find('li', class_='title').text.strip()
    # 提取文章的發布日期，位於class為'publish'的<li>標籤內
    date = articles.find('li', class_='publish').text.strip()
    # 提取文章的分類，位於class為'refer'的<ul>標籤內
    # 文字從第七個字符開始是因為前六個字符是"個人分類："，我們不需要
    sort = articles.find('ul',class_='refer').text[6:].strip()
    # 提取文章的圖片URL，位於<img>標籤的'src'屬性中
    img_src = articles.find('img')['src']
    
    # 將提取的數據以字典的形式添加到list中
    article.append({
        'Title': title,
        'Date': date,
        'Sort': sort,
        'Image URL': img_src,
    })

# 將存有所有文章信息的list轉換為pandas DataFrame
df = pd.DataFrame(article)

# 指定CSV檔案的儲存路徑
csv_file_path = 'article.csv'

# 將DataFrame儲存為CSV檔案，不保存索引，並設定編碼為utf-8-sig
df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

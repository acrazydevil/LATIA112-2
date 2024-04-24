# 引入必要的模組
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# 指定 Edge WebDriver 的路徑
service = Service('msedgedriver.exe')
driver = webdriver.Edge(service=service)

# 打開目標網站
driver.get('https://autos.yahoo.com.tw/new-cars/make/m-benz')

# 創建 WebDriverWait 的實例，用於後續的元素等待
# wait = WebDriverWait(driver, 10)

# 初始化一個列表用來儲存每輛車的資訊
cars=[]

# 遍歷頁面中所有的車輛元素
for car in driver.find_elements(By.CSS_SELECTOR, "div.year-single"):
    # 從每個車輛元素中提取標題（含年份）
    title = car.find_element(By.CLASS_NAME, "title").text.strip()
    # 從每個車輛元素中提取價格資訊
    price = car.find_element(By.CLASS_NAME, "price").text.strip()
    # 從每個車輛元素中提取圖片的URL
    image_url = car.find_element(By.TAG_NAME, "img").get_attribute("src").strip()
    
    # 將提取的資訊以字典的形式添加到之前創建的列表中
    cars.append({
        "Year": title[:4],  # 取標題字符串的前四個字符作為年份
        "Title": title[5:],  # 取標題字符串的第五個字符到最後作為車輛名稱
        "Price": price,  # 價格資訊
        "Image URL": image_url  # 圖片URL
    })

# 將爬取到的車輛資料轉換為 pandas DataFrame
df = pd.DataFrame(cars)
# 將 DataFrame 儲存為 CSV 文件，設定編碼為 utf_8_sig 以正確處理中文，並且不保存索引
df.to_csv("cars.csv", encoding='utf_8_sig', index=False)

# 關閉瀏覽器
driver.quit()

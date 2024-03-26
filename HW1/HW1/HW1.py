import pandas as pd  # 引入Pandas庫，用於資料處理
import matplotlib.pyplot as plt  # 引入Matplotlib庫，用於繪圖
from matplotlib.font_manager import fontManager  # 引入字型管理器，用於設置字型
import matplotlib as mpl  # 引入Matplotlib庫的pyplot模組，用於設置字型

# 第一個問題：顯示2023年台灣大專校院校學生數最多的前五大科系
def q1():
    df = pd.read_csv("112_sdata.csv")  # 讀取CSV檔案中的資料
    top_5_departments = df.groupby(["科系名稱"])["學生數"].sum().sort_values(ascending=False).head(5)  # 按科系名稱分組，計算學生數量並取前五名
    plt.bar(top_5_departments.index, top_5_departments.values, color="green")  # 繪製長條圖
    plt.title("Q1:2023年台灣大專校院校學生數最多的前五大科系")  # 設置圖表標題
    plt.xlabel("科系名稱")  # 設置X軸標籤
    plt.ylabel("學生數")  # 設置Y軸標籤
    plot_path_q1 = 'picture/Q1.png'  # 圖片保存路徑
    plt.savefig(plot_path_q1)  # 儲存圖片
    plt.show()  # 顯示圖表

# 第二個問題：顯示2023年台灣大專校院校博士最多的前五大科系
def q2():
    df = pd.read_csv("112_sdata.csv")  # 讀取CSV檔案中的資料
    doctoral_df = df[df['等級別'] == 'D 博士']  # 選取博士等級的資料
    top_5_departments = doctoral_df.groupby("科系名稱")["學生數"].sum().nlargest(5)  # 按科系名稱分組，計算學生數量並取前五名
    plt.figure(figsize=(10, 6))  # 設置圖表大小
    top_5_departments.plot(kind='bar', color='pink')  # 繪製長條圖
    plt.title('Q2:2023年台灣大專校院校博士最多的前五大科系')  # 設置圖表標題
    plt.xlabel('科系名稱')  # 設置X軸標籤
    plt.ylabel('學生數')  # 設置Y軸標籤
    plt.xticks(rotation=0)  # 設置X軸刻度標籤傾斜角度
    plt.tight_layout()  # 調整子圖參數，使圖像填滿整個圖像區域
    plot_path_q2 = 'picture/Q2.png'  # 圖片保存路徑
    plt.savefig(plot_path_q2)  # 儲存圖片
    plt.show()  # 顯示圖表

# 第三個問題：顯示2023年台灣大專校院校上學年度畢業生數最多的五大科系
def q3():
    df = pd.read_csv("112_sdata.csv")  # 讀取CSV檔案中的資料
    bachelor_df = df[df['等級別'] == 'B 學士']  # 選取學士等級的資料
    top_5_departments = bachelor_df.groupby(["科系名稱"])["上學年度畢業生數"].sum().sort_values(ascending=False).head(5)  # 按科系名稱分組，計算上學年度畢業生數量並取前五名
    plt.bar(top_5_departments.index, top_5_departments.values, color="gray")  # 繪製長條圖
    plt.title("Q3:2023年台灣大專校院校上學年度畢業生數最多的五大科系")  # 設置圖表標題
    plt.xlabel("科系名稱")  # 設置X軸標籤
    plt.ylabel("學生數")  # 設置Y軸標籤
    plot_path_q3 = 'picture/Q3.png'  # 圖片保存路徑
    plt.savefig(plot_path_q3)  # 儲存圖片
    plt.show()  # 顯示圖表

# 第四個問題：顯示2023年台灣大專校院校科系類別最多的五大學校
def q4():
    df = pd.read_csv("112_sdata.csv")  # 讀取CSV檔案中的資料
    total_departments_per_school = df.groupby("學校名稱")["科系名稱"].nunique()  # 按學校名稱分組，計算不同科系的數量
    top_5_schools = total_departments_per_school.nlargest(5)  # 取科系類別數量最多的前五名學校
    plt.figure(figsize=(10, 6))  # 設置圖表大小
    top_5_schools.plot(kind='bar', color='purple')  # 繪製長條圖
    plt.title('Q4:2023年台灣大專校院校科系類別最多的五大學校')  # 設置圖表標題
    plt.xlabel('學校名稱')  # 設置X軸標籤
    plt.ylabel('系所數量')  # 設置Y軸標籤
    plt.xticks(rotation=0)  # 設置X軸刻度標籤傾斜角度
    plt.tight_layout()  # 調整子圖參數，使圖像填滿整個圖像區域
    plot_path_q4 = 'picture/Q4.png'  # 圖片保存路徑
    plt.savefig(plot_path_q4)  # 儲存圖片
    plt.show()  # 顯示圖表

# 第五個問題：顯示2023年台灣大專校院校學校最多的五大縣市
def q5():
    df = pd.read_csv("112_sdata.csv")  # 讀取CSV檔案中的資料
    school_count_per_city = df.groupby("縣市名稱")["學校名稱"].nunique()  # 按縣市名稱分組，計算不同學校的數量
    top_5_cities = school_count_per_city.nlargest(5)  # 取學校數量最多的前五個縣市
    plt.figure(figsize=(10, 6))  # 設置圖表大小
    top_5_cities.plot(kind='bar', color='orange')  # 繪製長條圖
    plt.title('Q5:2023年台灣大專校院校學校最多的五大縣市')  # 設置圖表標題
    plt.xlabel('縣市名稱')  # 設置X軸標籤
    plt.ylabel('學校數量')  # 設置Y軸標籤
    plt.xticks(rotation=0)  # 設置X軸刻度標籤傾斜角度
    plt.tight_layout()  # 調整子圖參數，使圖像填滿整個圖像區域
    plot_path_q5 = 'picture/Q5.png'  # 圖片保存路徑
    plt.savefig(plot_path_q5)  # 儲存圖片
    plt.show()  # 顯示圖表

# 第六個問題：顯示2023年台灣大專校院校教師數最多的五大學校
def q6():
    df = pd.read_csv("112_sdata.csv")  # 讀取CSV檔案中的資料
    total_teachers_per_school = df.groupby("學校名稱")["教師數"].sum()  # 按學校名稱分組，計算教師數量
    top_5_schools = total_teachers_per_school.nlargest(5)  # 取教師數量最多的前五名學校
    plt.figure(figsize=(10, 6))  # 設置圖表大小
    top_5_schools.plot(kind='bar', color='blue')  # 繪製長條圖
    plt.title('Q6:2023年台灣大專校院校教師數最多的五大學校')  # 設置圖表標題
    plt.xlabel('學校名稱')  # 設置X軸標籤
    plt.ylabel('教師數量')  # 設置Y軸標籤
    plt.xticks(rotation=0)  # 設置X軸刻度標籤傾斜角度
    plt.tight_layout()  # 調整子圖參數，使圖像填滿整個圖像區域
    plot_path_q6 = 'picture/Q6.png'  # 圖片保存路徑
    plt.savefig(plot_path_q6)  # 儲存圖片
    plt.show()  # 顯示圖表

# 主函數：執行各個問題的函數並設置字型
def main():
    fontManager.addfont('NotoSansTC-Regular.ttf')  # 添加字型文件
    mpl.rc('font', family='Noto Sans TC')  # 設置字型

    q1()  # 執行第一個問題的函數
    q2()  # 執行第二個問題的函數
    q3()  # 執行第三個問題的函數
    q4()  # 執行第四個問題的函數
    q5()  # 執行第五個問題的函數
    q6()  # 執行第六個問題的函數

# 程式入口
if __name__ == '__main__':
    main()

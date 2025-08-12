import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
df = pd.read_csv("c:/Users/fysh4/OneDrive/桌面/De novo/COG.csv")

# 假設 CSV 中有兩個欄位：'FUNCYION' 和 'UNIGENE'
# 你可以修改這些欄位名為你的 CSV 中對應的欄位名

# 繪製橫條圖
plt.figure(figsize=(10, 6))  # 設定圖形大小
plt.barh(df['Function'], df['UNIGENE'], color='skyblue')  # 畫橫條圖

# 設定標題和軸標籤
plt.title('The COG Classification in DEG', fontsize=16)  # 設定標題
plt.ylabel('Function', fontsize=14)  # Y 軸標籤
plt.xlabel('Number of Unigenes', fontsize=14)  # X 軸標籤

# 顯示圖表
plt.tight_layout()  # 自動調整布局，避免標籤被截斷
plt.show()

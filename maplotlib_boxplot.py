import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

# 字型設定
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

big_table = pd.read_csv("C:\\Users\\DKJTR\\Desktop\\tag_score_standardize\\finished_big_table.csv")
big_table.fillna(0, inplace = True)
tag1 = big_table['新聞雜誌:商業與經濟新聞']
tag2 = big_table['地區:台灣北部']
tag3 = big_table['新聞雜誌:地方新聞']
tag4 = big_table['地區:日本']
tag5 = big_table['展覽:商務貿易']
tag6 = big_table['地區:歐美']
tag7 = big_table['生涯階段:工作階段(青壯年)']
tag8 = big_table['新聞雜誌:國際新聞']
tag9 = big_table['地區:台灣南部']
tag10 = big_table['旅遊:國內旅遊']


# 把資料序列畫成 boxplot
fig = plt.figure()
graph = plt.boxplot([tag1,tag2, tag3, tag4, tag5, tag6, tag7, tag8 ,tag9, tag10], labels = ['新聞雜誌:商業與經濟新聞',
                                                                                            '地區:台灣北部','新聞雜誌:地方新聞',
                                                                                            '地區:日本','展覽:商務貿易',
                                                                                            '地區:歐美','生涯階段:工作階段(青壯年)'
                                                                                            '新聞雜誌:國際新聞','地區:台灣南部'
                                                                                            '旅遊:國內旅遊'], sym='')
plt.boxplot([tag1,tag2, tag3, tag4, tag5, tag6, tag7, tag8 ,tag9, tag10], labels = ['新聞雜誌:商業與經濟新聞',
                                                                                            '地區:台灣北部','新聞雜誌:地方新聞',
                                                                                            '地區:日本','展覽:商務貿易',
                                                                                            '地區:歐美','生涯階段:工作階段(青壯年)'
                                                                                            '新聞雜誌:國際新聞','地區:台灣南部'
                                                                                            '旅遊:國內旅遊'], sym='')
plt.xticks(rotation = 45)
# plt.grid(axis = 'y')

for line in graph['medians']:
    # get position data for median line
    x, y = line.get_xydata()[0] # left of median line
    # overlay median value
    text(x, y, '%.1f' % y,
         ha='left')

for line in graph['boxes']:
    x, y = line.get_xydata()[0] # bottom of left line
    text(x, y, '%.1f' % y,
         va='bottom', 
         ha='left')     
    x, y = line.get_xydata()[3] # bottom of right line
    text(x, y, '%.1f' % y,
         va='bottom', # centered
             ha='left')
for line in graph['whiskers']:
    x, y = line.get_xydata()[1] # bottom of left line
    text(x, y, '%.1f' % y,
         va='bottom', 
         ha='left')     

plt.show()
plt.savefig("C:\\Users\\DKJTR\\Desktop\\tag_score_standardize\\result.png")

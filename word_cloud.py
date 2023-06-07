import re
from collections import Counter

import jieba
import pandas as pd
from wordcloud import WordCloud

# 读取Excel文件
df = pd.read_excel('EcustNews.xls', sheet_name='Sheet1')
# 选择detail列的数据
data = df['detail']
# 句子拼接
text = ''
for per_data in data:
    text = text + per_data
# 定义停用词列表，包含你想要去除的语气词
stop_words = ['的', '了', '和', '在', ' ', '与', '等', '为', '是']
# 去除标点符号
text = re.sub(r'[^\w\s]', '', text)
# 精确分词
words = jieba.lcut(text)
# 去除停用词
filtered_words = [word for word in words if word not in stop_words]
# 统计词频
word_freq = Counter(filtered_words)
# 获取前20个高频词
top_20_words = word_freq.most_common(20)
print(top_20_words)
# 生成词云图，并设置中文字体
wordcloud = WordCloud(width=800, height=400, background_color='white',
                      font_path='STXINWEI.TTF').generate_from_frequencies(dict(word_freq))
# 保存词云图为JPG图像文件
wordcloud_image = wordcloud.to_image()
wordcloud_image.save('词云图.jpg')

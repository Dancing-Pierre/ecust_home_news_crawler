import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('EcustNews.xls', sheet_name='Sheet1')
# 选择title列的数据
news_titles = df['title']

# 特征提取
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(news_titles)

# 聚类分析
k = 5  # 假设聚类数为5
kmeans = KMeans(n_clusters=k, n_init='auto')
kmeans.fit(tfidf_matrix)

# 获取聚类结果
cluster_labels = kmeans.labels_

# 使用PCA降维至2维以便可视化
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(tfidf_matrix.toarray())

# 可视化聚类结果
plt.figure(figsize=(10, 6))
scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=cluster_labels, cmap='rainbow')
plt.legend(handles=scatter.legend_elements()[0], labels=range(k))
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
plt.title('新闻聚类')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.savefig('聚类.png')

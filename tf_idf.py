import numpy as np
import pandas as pd
from IPython.display import Image, HTML
import matplotlib.pyplot as plt
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

listings = pd.read_csv('data.csv', usecols = ['MlsNumber', 'PublicRemarks', 'Type', 'Ammenities'])
#listings = listings.head(10)
#print(listings)

listings['PublicRemarks'] = listings['PublicRemarks'].astype('str')
listings['Type'] = listings['Type'].astype('str')
listings['Ammenities'] = listings['Ammenities'].astype('str')
#print(listings)

# Groupby by PublicRemarks
desc = listings.groupby("PublicRemarks")

# Summary statistic of all countries
desc.describe().head()

remarks_corpus = ' '.join(listings['PublicRemarks'])
type_corpus = ' '.join(listings['Type'])
amenities_corpus = ' '.join(listings['Ammenities'])

listings['content'] = listings[['PublicRemarks', 'Type', 'Ammenities']].astype(str).apply(lambda x: ' // '.join(x), axis = 1)
listings['content'].fillna('Null', inplace = True)

# Word Cloud
#name_wordcloud = WordCloud(stopwords = STOPWORDS, background_color = 'white', height = 2000, width = 4000).generate(desc_corpus)
#plt.figure(figsize = (16,8))
#plt.imshow(name_wordcloud)
#plt.axis('off')
#plt.show()

#TF-IDF for description
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(listings['content'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

results = {}
for idx, row in listings.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], listings['MlsNumber'][i]) for i in similar_indices]
    results[row['MlsNumber']] = similar_items[1:]

print(results)
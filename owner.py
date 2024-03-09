import streamlit as st
import pymongo
import json
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

# Disable WordCloud Warning
st.set_option('deprecation.showPyplotGlobalUse', False)
# MongoDB connection
client = pymongo.MongoClient(st.secrets["mongo_url"])
db = client['reviews']
collection = db['restaurant_reviews']


image = Image.open(r'logo.png')
st.image(image, use_column_width=True)
st.title('Opinion Optics - Owner Statistics')

# Retrieve recent reviews from MongoDB
recent_reviews_cursor = collection.find().sort('_id', pymongo.DESCENDING).limit(10)
recent_reviews = list(recent_reviews_cursor)

# Display overall statistics
total_reviews = collection.count_documents({})
positive_reviews = collection.count_documents({'Sentiment': 'Positive'})
negative_reviews = collection.count_documents({'Sentiment': 'Negative'})

# Create pie chart for sentiment distribution
sentiment_data = [positive_reviews, negative_reviews]
labels = ['Positive', 'Negative']

fig1, ax1 = plt.subplots()
ax1.pie(sentiment_data, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  
st.subheader('Sentiment Distribution:')
st.pyplot(fig1)

st.subheader('Overall Statistics:')
st.write(f"Total Reviews: {total_reviews}")
st.write(f"Positive Reviews: {positive_reviews}")
st.write(f"Negative Reviews: {negative_reviews}")

# Display recent negative and recent positive comments
recent_negative_reviews = collection.find({'Sentiment': 'Negative'}).sort('_id', pymongo.DESCENDING).limit(5)
recent_positive_reviews = collection.find({'Sentiment': 'Positive'}).sort('_id', pymongo.DESCENDING).limit(5)

st.subheader('Recent Negative Comments:')
for idx, review in enumerate(recent_negative_reviews, start=1):
    st.write(f"{review['Review']}")
    st.write('---')

st.subheader('Recent Positive Comments:')
for idx, review in enumerate(recent_positive_reviews, start=1):
    st.write(f"{review['Review']}")
    st.write('---')

# Separate positive and negative reviews and extract text data
negative_reviews = collection.find({'Sentiment': 'Negative'}).sort('_id', pymongo.DESCENDING)
positive_reviews= collection.find({'Sentiment': 'Positive'}).sort('_id', pymongo.DESCENDING)

negative_reviews_text = ' '.join(review['Review'] for review in list(negative_reviews))
positive_reviews_text = ' '.join(review['Review'] for review in list(positive_reviews))


# Generate word clouds
negative_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(negative_reviews_text)
positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews_text)

# Display word clouds
st.subheader('Word Cloud for Positive Reviews:')
plt.figure(figsize=(10, 5))
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot()

st.subheader('Word Cloud for Negative Reviews:')
plt.figure(figsize=(10, 5))
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot()


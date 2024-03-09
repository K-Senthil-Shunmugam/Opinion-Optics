import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from PIL import Image
import json
import pymongo




# Define HyperParameters
vocab_size = 10000
max_length = 100
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"

# Load the sentiment analysis model
model = load_model('sentiment_analysis_model.h5')

# Read from JSON file
with open('Vocabulary.json', 'r') as json_file:
    loaded_X_train_list = json.load(json_file)

# Convert Python lists back to NumPy arrays
X_train = np.array(loaded_X_train_list)

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(X_train)

# MongoDB connection
client = pymongo.MongoClient(st.secrets["mongo_url"])
# Replace 'your_mongo_connection_string' with your MongoDB connection string
db = client['reviews']
collection = db['restaurant_reviews']

# Streamlit app

# Load the image
image = Image.open(r'logo.png')

# Display the image
st.image(image, use_column_width=True)

st.title('Opinion Optics-Review Portal')

# Get user input
user_review = st.text_area('Leave your review here:')




if st.button('Submit'):
    # Tokenize and pad the user's input
    sequences = tokenizer.texts_to_sequences([user_review])
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    # Make prediction
    prediction = model.predict(padded)[0][0]
    sentiment = 'Positive' if prediction >= 0.5 else 'Negative'

    # Display result
    st.write(f"Review: {user_review}")
    st.write(f"Sentiment: {sentiment}")

    # Save the review and sentiment to MongoDB
    review_data = {'Review': user_review, 'Sentiment': sentiment, 'Score': float(prediction)}  # Convert to Python float
    collection.insert_one(review_data)
    st.success('Review Updated')


# Display recent 10 comments
recent_reviews = collection.find().sort('_id', pymongo.DESCENDING).limit(10)

st.subheader('Recent Comments:')
for idx, review in enumerate(recent_reviews, start=1):
    st.write(f"{review['Review']}")
    st.write('---')



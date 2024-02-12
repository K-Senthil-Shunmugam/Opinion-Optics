# Opinion Optics - Restaurant Review Analysis

Opinion Optics is an online restaurant review portal designed to provide analytics and insights to restaurant owners by analyzing customer reviews using Natural Language Processing (NLP) techniques. This repository contains the codebase for the sentiment analysis model, web application, and instructions to run the application locally.

## Try out the App 

  - Owner Page - https://opinion-optics-owner.streamlit.app/
  - Customer Page - https://opinion-optics-customer.streamlit.app/

## Web Application Overview

The web application consists of two main components:

1. **Customer Portal (`customer.py`):**
   - Allows customers to input their reviews.
   - Performs sentiment analysis on the submitted review.
   - Displays the sentiment (positive/negative) of the review.
   - Saves the review and sentiment to a MongoDB database.
   - Displays recent positive and negative comments.

2. **Owner Statistics (`owner.py`):**
   - Provides restaurant owners with analytics and insights.
   - Displays the overall sentiment distribution of reviews.
   - Shows overall statistics including the total number of reviews, positive reviews, and negative reviews.
   - Displays recent negative and positive comments.

## Instructions to Run the Application

1. **Clone the Repository:**

2. **Install Dependencies:**
pip install -r requirements.txt
3. **Setup MongoDB:**
- Install MongoDB and start the MongoDB service.
- Create a new database named `reviews`.
- Create a collection named `restaurant_reviews` within the `reviews` database.
- Update the connection string in the `secrets.toml` file.

4. **Run the Customer Portal:**
streamlit run customer.py
- Access the customer portal via the provided URL.

5. **Run the Owner Statistics Dashboard:**
- Access the owner statistics dashboard via the provided URL.

### Model Architecture: Sequential Model with Embedding Layer and Dense Layers

The sentiment analysis model follows a sequential architecture(Simple Artifical Neural Network) with the following components:

1. **Embedding Layer:** Converts words into dense vectors of fixed size, capturing semantic meaning and relationships between words.
  
2. **Global Average Pooling Layer:** Reduces the dimensionality of the input data by averaging the embeddings across all words in each review.

3. **Dense Layers:** A series of dense (fully connected) layers with rectified linear unit (ReLU) activation functions to learn complex patterns and relationships in the data.

4. **Output Layer:** A single dense layer with a sigmoid activation function, producing a probability score indicating the likelihood that a review expresses positive sentiment.

This architecture is commonly used for text classification tasks like sentiment analysis, where the goal is to classify text into predefined categories or predict a continuous value based on text inputs.

### Model Metrics: 

![image](https://github.com/K-Senthil-Shunmugam/Opinion-Optics/assets/113205555/2356c371-a002-49c1-9c2d-66a9f1fcb743)

![image](https://github.com/K-Senthil-Shunmugam/Opinion-Optics/assets/113205555/c4b84aff-8fb1-4c38-8a4c-8305493a9631)


## Training the Sentiment Analysis Model (Model.ipynb)

To train the sentiment analysis model for your own dataset, follow these instructions:

1. **Ensure Dependencies:**
   - Make sure you have Jupyter Notebook installed along with the required Python libraries mentioned in the provided `Model.ipynb` file.

2. **Prepare Your Dataset:**
   - you can download the Dataset used in this project either from this [git-repo](DataSet.csv) or from Kaggle
     https://www.kaggle.com/datasets/d4rklucif3r/restaurant-reviews
   - Load the sample dataset (`DataSet.csv`) or Replace it with your own dataset containing two columns: one for the reviews and one for the corresponding labels (positive/negative).

4. **Run the Notebook:**
   - Open the `Model.ipynb` notebook in Jupyter Notebook.
   - Execute each cell in the notebook sequentially to load the dataset, preprocess the data, train the model, and save the trained model.

5. **Adjust Hyperparameters (Optional):**
   - You can adjust the hyperparameters such as vocabulary size, embedding dimension, maximum sequence length, and number of epochs according to your requirements.

6. **Save the Trained Model:**
   - After training, the model will be saved as `sentiment_analysis_model.h5` in the same directory.
   - You can use this trained model for inference in the customer portal (`customer.py`) provided in this repository.

7. **Evaluate Model Performance (Optional):**
   - Optionally, you can evaluate the performance of your trained model on a separate test dataset to assess its accuracy and other metrics.

8. **Customize as Needed:**
   - Feel free to customize the notebook or extend the functionality based on your specific requirements.
   - You can also integrate additional features or improve the model architecture for better performance.


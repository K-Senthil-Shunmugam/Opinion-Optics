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
git clone <repository_url>
2. **Install Dependencies:**
pip install -r requirements.txt
3. **Setup MongoDB:**
- Install MongoDB and start the MongoDB service.
- Create a new database named `reviews`.
- Create a collection named `restaurant_reviews` within the `reviews` database.

4. **Run the Customer Portal:**
streamlit run customer.py
- Access the customer portal via the provided URL.

5. **Run the Owner Statistics Dashboard:**
- Access the owner statistics dashboard via the provided URL.

## Training the Sentiment Analysis Model (Model.ipynb)

To train the sentiment analysis model for your own dataset, follow these instructions:

1. **Ensure Dependencies:**
   - Make sure you have Jupyter Notebook installed along with the required Python libraries mentioned in the provided `Model.ipynb` file.

2. **Prepare Your Dataset:**
   - you can download the Dataset used in this project either from this [git-repo](DataSet.csv) or from Kaggle
     https://www.kaggle.com/datasets/d4rklucif3r/restaurant-reviews
   - Replace the sample dataset (`DataSet.csv`) with your own dataset containing two columns: one for the reviews and one for the corresponding labels (positive/negative).
   - Ensure that your dataset is in CSV format and is accessible from the same directory as the notebook.
   - I got the dataset from 

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


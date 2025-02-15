import nltk 
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import string
import random

# nltk.download('movie_reviews')
# nltk.download('stopwords')
vectorizer = CountVectorizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return ' '.join(filtered_tokens)

corpus = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
vectorizer.fit_transform([preprocess_text(text) for text in corpus])    

#using naive bayes classifier model
from sklearn.naive_bayes import MultinomialNB
corpus = [(preprocess_text(movie_reviews.raw(fileid)),category) for category in movie_reviews.categories()
          for fileid in movie_reviews.fileids(category)]

random.shuffle(corpus)

texts,labels = zip(*corpus)

X = vectorizer.fit_transform(texts)
clf = MultinomialNB()
clf.fit(X,labels)

def generate_response(user_input):
    # Preprocess and tokenize the user input
    preprocessed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([preprocessed_input])
    # Use the classifier to predict a response
    predicted_category = clf.predict(input_vector)[0]
    # Choose a random movie review from the predicted category
    reviews_in_category = movie_reviews.fileids(predicted_category)
    review_id = random.choice(reviews_in_category)
    review_text = movie_reviews.raw(review_id)
    # Return the review text as the chatbot response
    return review_text


import pandas as pd
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')

# Load dataset
data = pd.read_csv("faqs.csv")

questions = data['Question'].tolist()
answers = data['Answer'].tolist()

print(data)

# Text preprocessing function
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Preprocess questions
processed_questions = [preprocess(q) for q in questions]

# Convert text to vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot function
def chatbot(user_input):
    user_input = preprocess(user_input)
    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, faq_vectors)
    best_match = similarity.argmax()
    score = similarity[0][best_match]

    if score > 0.3:
        return answers[best_match]
    else:
        return "Sorry, I couldn't find an answer."

# Chat interface
print("FAQ Chatbot is running...")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot(user)
    print("Bot:", response)
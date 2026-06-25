FAQ Chatbot using NLP

This is a simple FAQ Chatbot built using Python. The chatbot answers user questions based on a predefined FAQ dataset using Natural Language Processing (NLP).


1. Features

   1) Loads FAQ data from CSV file
   2) Uses NLP techniques for text preprocessing
   3) TF-IDF vectorization for text conversion
   4) Cosine similarity to find best matching answer
   5) Simple command-line chatbot interface

   
2. Technologies Used

   1) Python
   2) Pandas
   3) NLTK
   4) Scikit-learn


3. Project Structure
   1) FAQChatbot.py → Main Python file
   2) faqs.csv → FAQ dataset


4. How to Run the Project
   
   1) Download or clone the project folder
   2) Open terminal in the project folder
   3) Install required libraries using command:
      pip install pandas nltk scikit-learn
   4) Run the chatbot using command:
      python FAQChatbot.py
      

 6. How it Works
    
    1) User enters a question
    2) System preprocesses the text
    3) Converts text into numerical vectors (TF-IDF)
    4) Finds the most similar FAQ using cosine similarity
    5) Returns the best matching answer
       
      
8. Example
   
   You: What is AI?
   Bot: AI stands for Artificial Intelligence.


   You: Who can join this course?
   Bot: Anyone interested in AI including beginners and professionals.

   
Author:
Sakshi Bondre

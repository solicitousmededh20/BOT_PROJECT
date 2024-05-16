# 

import pandas as pd 
import speech_recognition as sr
from gtts import gTTS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import os
import time

# Load the dataset
df = pd.read_excel('IT TECHNOLOGY (12).xlsx')
if df.isnull.sum()<=0:
    df=df
else :
    df = df.dropna()
    df.columns = df.iloc[0]
    df = df[1:]
#Function to select a question based on the level type
def select_question(level_type):
    filtered_df = df[df['Level Type'] == level_type]
    if filtered_df.empty:
        print("No questions found for the selected level type.")
        return None, None
    else:
        question_row = filtered_df.sample(n=1)
        question = question_row['Question'].values[0]
        correct_answer = question_row['Answer'].values[0]
        level_type_display = question_row['Level Type'].values[0]
        sr_no = question_row['Sr. No'].values[0]
        return question, correct_answer, level_type_display, sr_no
        

# Compute similarity between user answer and dataset answer
def compute_similarity(user_answer, dataset_answer):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([user_answer, dataset_answer])
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return similarity_score

# Function to recognize speech input from the user
def speech_to_text():
    recognizer = sr.Recognizer()
    
    # Delay the start by 15 seconds
    print("Waiting for 15 seconds before starting speech recognition...")
    time.sleep(30)
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=10)  # Stop listening after 10 seconds of speech
        except sr.WaitTimeoutError:
            print("No speech detected after 10 seconds. Stopping...")
            return ""
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Sorry, there was an error processing your request:", str(e))



# Main function
def main():
    level_type =input('choose the level type like Basic/Intermediate/Expert: ')
    while True:
        #   # Set level type to basic for this example
        # filtered_df = df[df['Level Type'] == level_type]
        # if filtered_df.empty:
        #     print("No questions found for the selected level type.")
        #     return

        # question_row = filtered_df.sample(n=1)
        # question = question_row['Question'].values[0]
        # correct_answer = question_row['Answer'].values[0]
        # level_type_display = question_row['Level Type'].values[0]
        # sr_no = question_row['Sr. No'].values[0]
        # question=df['Question'][sr_no]
        question, correct_answer, level_type_display, sr_no=select_question(level_type)

        # Using gTTS to make the bot ask the question
        tts = gTTS(text=question, lang='en')
        print("Bot: Asking the question...")
        print("Question:", question)
        tts.save("question.mp3")
        os.system("start question.mp3")

        # Using speech recognition for user's answer
        #user_answer=select_question(level_type)
        user_answer=input('user answer: ')
        # print("you can speak now")
        print("Question:", question)
        print("Correct answer:", correct_answer)
        # print("Your answer:", user_answer)
        print('level_type:', level_type_display)
        print('sr_no',sr_no)
        print("question",question)
        user_answer=input("enter the answer here : ")
        
        # Compute similarity between user's answer and correct answer
        similarity_score = compute_similarity(user_answer, correct_answer)
        
        similarity_score = round(similarity_score, 1)  # Round to one digit after the decimal
        similarity_score = similarity_score * 10   
        print("Similarity score:", similarity_score,'/10')

        # print("Question:", question)
        # print("Correct answer:", correct_answer)
        # # print("Your answer:", user_answer)
        # print('level_type:', level_type_display)
        # print('sr_no',sr_no)
        # print("question",question)
        print("Your answer:", user_answer)

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main() 
# import pandas as pd 
# import speech_recognition as sr
# from gtts import gTTS
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import os
# import time

# # Load the dataset
# df = pd.read_excel('IT TECHNOLOGY (12).xlsx')
# if df.isnull().sum().sum() <= 0:
#     df = df
# else:
#     df = df.dropna()
#     df.columns = df.iloc[0]
#     df = df[1:]

# # Function to select a question based on the level type
# def select_question(level_type):
#     filtered_df = df[df['Level Type'] == level_type]
#     if filtered_df.empty:
#         print("No questions found for the selected level type.")
#         return None, None, None, None
#     else:
#         question_row = filtered_df.sample(n=1)
#         question = question_row['Question'].values[0]
#         correct_answer = question_row['Answer'].values[0]
#         level_type_display = question_row['Level Type'].values[0]
#         sr_no = question_row['Sr. No'].values[0]
#         return question, correct_answer, level_type_display, sr_no

# # Compute similarity between user answer and dataset answer
# def compute_similarity(user_answer, dataset_answer):
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform([user_answer, dataset_answer])
#     similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
#     return similarity_score

# # Function to recognize speech input from the user
# def speech_to_text():
#     recognizer = sr.Recognizer()
    
#     # Delay the start by 15 seconds
#     print("Waiting for 15 seconds before starting speech recognition...")
#     time.sleep(15)
    
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         try:
#             audio = recognizer.listen(source, timeout=10)  # Stop listening after 10 seconds of speech
#         except sr.WaitTimeoutError:
#             print("No speech detected after 10 seconds. Stopping...")
#             return ""
    
#     try:
#         text = recognizer.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#         return ""
#     except sr.RequestError as e:
#         print("Sorry, there was an error processing your request:", str(e))
#         return ""

# # Main function
# def main():
#     level_type = input('Choose the level type (Basic/Intermediate/Expert): ')
#     while True:
#         question, correct_answer, level_type_display, sr_no = select_question(level_type)
#         if question is None:
#             break

#         # Using gTTS to make the bot ask the question
#         tts = gTTS(text=question, lang='en')
#         print("Bot: Asking the question...")
#         tts.save("question.mp3")
#         os.system("start question.mp3")

#         # Using speech recognition for user's answer
#         print("You can speak now.")
#         user_answer = speech_to_text()
#         if user_answer == "":
#             continue
        
#         # Compute similarity between user's answer and correct answer
#         similarity_score = compute_similarity(user_answer, correct_answer)
#         similarity_score = round(similarity_score * 10, 1)  # Scale to 10-point score

#         print("Similarity score:", similarity_score, "/10")
#         print("Question:", question)
#         print("Correct answer:", correct_answer)
#         print("Your answer:", user_answer)
#         print('Level type:', level_type_display)
#         print('Sr. No:', sr_no)

#         choice = input("Do you want to continue? (yes/no): ")
#         if choice.lower() != 'yes':
#             break

# if __name__ == "__main__":
#     main()


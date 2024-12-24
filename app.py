import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Load the trained models and vectorizer
nb_model = pickle.load(open('nb_model.pkl', 'rb'))
log_reg_model = pickle.load(open('log_reg_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ""
    nb_result = None
    nb_proba = None
    log_reg_result = None
    log_reg_proba = None

    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.form['text']
        
        # Preprocess the user input (same preprocessing as for training)
        processed_input = preprocess_text(user_input)
        
        # Transform the input text using the vectorizer
        input_vector = vectorizer.transform([processed_input]).toarray()

        # Get predictions from the models
        nb_pred = nb_model.predict(input_vector)[0]
        nb_proba = nb_model.predict_proba(input_vector)[0][1]  # Probability of being cyberbullying

        log_reg_pred = log_reg_model.predict(input_vector)[0]
        log_reg_proba = log_reg_model.predict_proba(input_vector)[0][1]  # Probability of being cyberbullying

        # Convert predictions to readable labels
        nb_result = "Cyberbullying" if nb_pred == 1 else "Not Cyberbullying"
        log_reg_result = "Cyberbullying" if log_reg_pred == 1 else "Not Cyberbullying"

    return render_template('index.html', 
                           user_input=user_input,
                           nb_result=nb_result,
                           nb_proba=nb_proba,
                           log_reg_result=log_reg_result,
                           log_reg_proba=log_reg_proba)

def preprocess_text(text):
    # Preprocessing: lowercase, remove non-alphanumeric characters, remove stopwords
    stop_words = set(["the", "and", "is", "in", "to", "for", "on", "a", "it", "that"])  # Add more stopwords if needed
    text = text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

if __name__ == '__main__':
    app.run(debug=True)

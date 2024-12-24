# TwitSafe: A Machine Learning-Based Cyberbullying Detection System for Twitter

TwitSafe is a research-driven project designed to detect cyberbullying on Twitter using advanced machine learning techniques. This repository contains the implementation of the project, including the web application, machine learning models, and the corresponding research paper.

---

## 📄 Research Paper

For detailed insights into the methodology, experiments, and findings of this project, please refer to the [published paper](TwitSafe_Paper.pdf).  
If citing this work, please use the following format:

```
[Your Citation Format Here – Add BibTeX or other formats]
```

---

## 🚀 Features

- **Web Interface**: A user-friendly web app to detect cyberbullying in text.
- **Machine Learning Models**: Pre-trained Logistic Regression and Naive Bayes models for text classification.
- **Dataset**: A curated dataset for cyberbullying detection.
- **Model Files**: Includes pre-trained models and vectorizer for easy deployment.

---

## 📂 Project Structure

```
TwitSafe/
│
├── templates/          # Contains HTML templates for the web application
│   └── index.html      # Main web interface
├── app.py              # Flask application to run the web app
├── cyberbullying_data.csv # Dataset used for training and testing
├── log_reg_model.pkl   # Pre-trained Logistic Regression model
├── nb_model.pkl        # Pre-trained Naive Bayes model
├── vectorizer.pkl      # Vectorizer for text preprocessing
├── main.ipynb          # Jupyter notebook for experimentation and training
├── TwitSafe_Paper.pdf  # Research paper on the project
└── README.md           # Project documentation
```

---

## 🔧 Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/reekankshap/TwitSafe.git
   cd TwitSafe
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask web application:
   ```bash
   python app.py
   ```

4. Open the web app in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## 💻 Usage

- **Web Application**: Enter text in the web interface to check if it contains cyberbullying.
- **Notebook**: Use `main.ipynb` for model training, evaluation, and experimentation.

---

## 📊 Results and Visualizations

The results of the trained models, along with metrics such as precision, recall, and F1-score, are detailed in the research paper. Additional visualizations can be created using the notebook.

---

## 🤝 Contributing

We welcome contributions! If you want to improve this project, feel free to:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Submit a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌐 Citation

If you find this project helpful, please consider citing our work:
```
[Your Citation Here]
```

---

## 📬 Contact

For inquiries, please contact [reekankshaprakash@gmail.com]. You can also connect via LinkedIn.

# TwitSafe
A Machine Learning-Based Cyberbullying Detection System for Twitter

TwitSafe is a research-driven project designed to detect cyberbullying on Twitter using advanced machine learning techniques. This repository contains the implementation of the project, including data preprocessing, model training, evaluation, and the corresponding research paper.

---

## 📄 Research Paper

For detailed insights into the methodology, experiments, and findings of this project, please refer to the [published paper](TwitSafe_Paper.pdf).  
If citing this work, please use the following format:

```
[Your Citation Format Here – Add BibTeX or other formats]
```

---

## 🚀 Features

- **Data Preprocessing**: Handles raw Twitter data to prepare it for model training.
- **Machine Learning Models**: Implements various ML algorithms for text classification.
- **Evaluation Metrics**: Includes precision, recall, F1-score, and confusion matrix for detailed model evaluation.
- **Interactive Visualizations**: Visualizes dataset distributions and model performance.

---

## 📂 Project Structure

```
TwitSafe/
│
├── datasets/          # Contains raw and processed Twitter data
├── models/            # Trained models and saved configurations
├── scripts/           # Python scripts for preprocessing, training, and evaluation
├── docs/              # Research paper and supplementary materials
├── results/           # Outputs, logs, and visualizations
└── README.md          # Project documentation
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

3. Download the dataset:
   - Add the dataset to the `cyberbullying_data.csv` file.

4. Run the preprocessing script:
   ```bash
   python scripts/preprocess.py
   ```

5. Train the model:
   ```bash
   python scripts/train.py
   ```

6. Evaluate the model:
   ```bash
   python scripts/evaluate.py
   ```

---

## 💻 Usage

- **Detect Cyberbullying**: 
   Use the pre-trained model to detect cyberbullying in custom datasets or real-time Twitter data:
   ```bash
   python scripts/detect.py --input your_twitter_data.csv
   ```

- **Interactive Dashboard**: 
   Start a web dashboard to visualize results:
   ```bash
   streamlit run scripts/dashboard.py
   ```

---

## 📊 Results and Visualizations

Key results and visualizations are available in the `results/` folder, showcasing:
- Dataset analysis
- Model performance metrics
- Case studies of detected tweets

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

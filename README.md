# 📱 Phone Price Prediction

This project predicts the price of a smartphone based on its specifications like brand, RAM, storage, camera, etc. The dataset was generated using web scraping and the model is
📦 phone-price-prediction/
    ├── files/
    │ ├── CleanedData.csv
    │ ├── final_data.csv
    │ ├── mobiles.csv
    │ ├── model.pkl
    │ ├── phone_links.npy
    │ └── pipe.pkl
    ├── static/
    │ └── style.css
    ├── templates/
    │ └── index.html
    ├── app.py
    ├── form.py
    ├── helper.txt
    ├── data_collection.ipynb
    ├── data_cleaning.ipynb
    ├── model_training.ipynb
    ├── requirements.txt
    └── README.md


---

## ⚙️ Features

- 🧹 Scraped and cleaned smartphone data using BeautifulSoup
- 📈 Trained regression model using scikit-learn pipeline
- 💻 Simple web interface for predicting phone prices
- 🗃️ Includes data pipeline for reproducibility

---

## 📊 Tech Stack

- Python (pandas, scikit-learn, BeautifulSoup)
- Flask (for the web app)
- HTML/CSS (for frontend)
- Jupyter Notebooks (for data processing and model training)

---

## 🔍 Workflow

1. **Data Collection**:  
   Web scraping using `data_collection.ipynb`, saved to `mobiles.csv`.

2. **Data Cleaning & Preprocessing**:  
   Cleaning with `data_cleaning.ipynb`, final features saved in `final_data.csv`.

3. **Model Training**:  
   Model trained in `model_training.ipynb`, saved as `model.pkl` and pipeline as `pipe.pkl`.

4. **Web Interface**:  
   Flask app (`app.py`) loads the pipeline and predicts based on user input from the HTML form.

---

## 🚀 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/phone-price-prediction.git
cd phone-price-prediction

pip install -r requirements.txt

python app.py
```
Open browser and navigate to <br>
http://127.0.0.1:5000/

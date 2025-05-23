# Email Spam Detection System

A full-stack machine learning pipeline to classify emails as Spam or Ham. This project performs end-to-end email processing including data scraping, text preprocessing, clustering for insight, model training and saving, and an optional alert system for suspicious messages.

## Features

- Scrapes email data from online sources or files
- Cleans and preprocesses text using NLP
- Clusters similar spam messages using unsupervised learning
- Trains and evaluates classification models
- Saves trained models for later use
- Optional real-time alert system via email/SMS/desktop notifications
- Streamlit frontend for interactive use

## Tech Stack

- Python 3.10+
- pandas, numpy – data manipulation
- scikit-learn – machine learning
- nltk / spacy – NLP processing
- beautifulsoup4, requests – web scraping
- matplotlib, seaborn – optional visualizations
- joblib – model serialization
- smtplib / twilio / plyer – alerting
- Streamlit – Web frontend

## Workflow Overview

1. Scrape or load emails
2. Clean and preprocess text data
3. Convert text to numerical features using TF-IDF
4. (Optional) Cluster messages for analysis
5. Train a classifier to distinguish spam from ham
6. Save the model for future use
7. Use the saved model for predictions
8. Trigger alerts for detected spam if needed
9. Deploy frontend via Streamlit

## Project Structure

```
Email_Spam_Detection/
├── main.py                 # Streamlit app entry point
├── data_scraper.py         # Web/email scraping logic
├── preprocessing.py        # Text cleaning & NLP pipeline
├── clustering.py           # KMeans or DBSCAN clustering
├── train_model.py          # Train & evaluate model
├── model/                  
│   └── spam_model.pkl      # Saved trained model
├── alerting.py             # Alert system (email/SMS/notification)
├── utils.py                # Helper functions
├── predict.py              # Run prediction on new emails
├── requirements.txt        
└── README.md
```

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/sreehari1004/Email_Spam_Detection.git
cd Email_Spam_Detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline

```bash
python data_scraper.py
python preprocessing.py
python clustering.py
python train_model.py
```

### 4. Use CLI Prediction

```bash
python predict.py --input "Congratulations! You've won a prize..."
```

## Streamlit Deployment

You can run the interactive web app using Streamlit.

### To Run Locally:

```bash
streamlit run main.py
```

### To Deploy Online:

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **"New App"**
3. Set the following:
   - **Repository:** `sreehari1004/Email_Spam_Detection`
   - **Branch:** `master`
   - **Main file path:** `main.py`
4. Click **"Deploy"**

Once deployed, your app will be accessible at:

```
https://emailspamdetection-bkyaa42amb7mqysy8d7rnj.streamlit.app/
```

## Model Performance

| Metric    | Score   |
|-----------|---------|
| Accuracy  | 97.8%   |
| Precision | 96.5%   |
| Recall    | 98.2%   |
| F1 Score  | 97.3%   |

## Alerting Options

- Email alerts via `smtplib`
- SMS alerts via Twilio API
- Desktop popups via `plyer`

These options can be configured in `alerting.py`.

## Future Improvements

- Integrate with Gmail API for real-time scanning
- Add a database to track flagged messages
- Use deep learning models like BERT for better classification
- Improve UI/UX with user authentication and logging
- Deploy to cloud platforms (AWS/GCP) with Docker

## Credits

- UCI SMS Spam Collection Dataset
- scikit-learn documentation
- Twilio / Plyer APIs
- Tutorials and open-source projects for inspiration

## Contact

Author: Sreehari  
GitHub: [sreehari1004](https://github.com/sreehari1004)

Feel free to open issues or submit pull requests to contribute.

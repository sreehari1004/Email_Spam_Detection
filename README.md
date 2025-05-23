# Email Spam Detection System

A full-stack machine learning pipeline to classify emails as Spam or Ham. This project performs end-to-end email processing including data scraping, text preprocessing, clustering for insight, model training and saving, and an optional alert system for suspicious messages.

## Features

- Scrapes email data from online sources or files
- Cleans and preprocesses text using NLP
- Clusters similar spam messages using unsupervised learning
- Trains and evaluates classification models
- Saves trained models for later use
- Optional real-time alert system via email/SMS/desktop notifications

## Tech Stack

- Python 3.10+
- pandas, numpy – data manipulation
- scikit-learn – machine learning
- nltk / spacy – NLP processing
- beautifulsoup4, requests – web scraping
- matplotlib, seaborn – optional visualizations
- joblib – model serialization
- smtplib / twilio / plyer – alerting

## Workflow Overview

1. Scrape or load emails
2. Clean and preprocess text data
3. Convert text to numerical features using TF-IDF
4. (Optional) Cluster messages for analysis
5. Train a classifier to distinguish spam from ham
6. Save the model for future use
7. Use the saved model for predictions
8. Trigger alerts for detected spam if needed

## Project Structure

```
Email_Spam_Detection/
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

## How to Run

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
python data_scraper.py         # Step 1: Scrape data
python preprocessing.py        # Step 2: Clean and preprocess
python clustering.py           # Step 3: (Optional) Clustering
python train_model.py          # Step 4: Train and save model
```

### 4. Run Prediction with Alert

```bash
python predict.py --input "Congratulations! You've won a prize..."
```

## Example Output

```
[INFO] Message classified as SPAM
[ALERT] Suspicious content detected. Alert triggered.
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
- Add a web-based frontend using Streamlit or Flask
- Use deep learning models like BERT for improved classification
- Deploy to a cloud platform for scalability

## Credits

- UCI SMS Spam Collection Dataset
- scikit-learn documentation
- Twilio / Plyer APIs
- Tutorials and open-source projects for inspiration

## Contact

Author: Sreehari  
GitHub: https://github.com/sreehari1004

Feel free to open issues or submit pull requests to contribute.

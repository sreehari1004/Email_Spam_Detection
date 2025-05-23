import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def preprocess_dataframe(df):
    df['clean_message'] = df['message'].apply(clean_text)
    return df

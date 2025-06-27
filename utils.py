import re

def clean_text(text):
    text = re.sub(r'<[^>]*?>', '', text)                                                                          # Remove html tags
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)                                                                     # Remove special character
    text = text.strip()                                                                                           # Remove extra whitespace
    text = ' '.join(text.split())                                                                                 # Remove extra whitespace

    return text
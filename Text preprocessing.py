import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import download
download('punkt')
download('stopwords')
download('wordnet')
import nltk
nltk.download('punkt')
import nltk
nltk.download('punkt_tab')
# Sample text
text = """Hello! I'm new to NLP. Let's process this text. Visit https://www.example.com for details. 
         Send your queries to help@nlp.com or call 123-456-7890. Text preprocessing is fun, especially when done correctly."""

# 1. Convert to lowercase
text_lower = text.lower()
print("1. Lowercase Text:")
print(text_lower)

# 2. Remove URLs and email addresses
text_no_urls_emails = re.sub(r'https?://\S+|www\.\S+|[\w.-]+@[\w.-]+', '', text_lower)
print("\n2. Remove URLs and Email Addresses:")
print(text_no_urls_emails)

# 3. Remove numbers
text_no_numbers = re.sub(r'\d+', '', text_no_urls_emails)
print("\n3. Remove Numbers:")
print(text_no_numbers)

# 4. Remove punctuation
text_no_punctuation = text_no_numbers.translate(str.maketrans('', '', string.punctuation))
print("\n4. Remove Punctuation:")
print(text_no_punctuation)

# 5. Tokenization
tokens = word_tokenize(text_no_punctuation)
print("\n5. Tokenization:")
print(tokens)

# 6. Remove stopwords
stop_words = set(stopwords.words('english'))
tokens_no_stopwords = [word for word in tokens if word not in stop_words]
print("\n6. Remove Stopwords:")
print(tokens_no_stopwords)

# 7. Lemmatization
lemmatizer = WordNetLemmatizer()
tokens_lemmatized = [lemmatizer.lemmatize(word) for word in tokens_no_stopwords]
print("\n7. Lemmatization:")
print(tokens_lemmatized)

# 8. Stemming (Optional, use either stemming or lemmatization based on the task)
stemmer = PorterStemmer()
tokens_stemmed = [stemmer.stem(word) for word in tokens_no_stopwords]
print("\n8. Stemming:")
print(tokens_stemmed)

# 9. Remove short tokens (Optional, e.g., remove single-character tokens)
tokens_filtered = [word for word in tokens_stemmed if len(word) > 1]
print("\n9. Remove Short Tokens:")
print(tokens_filtered)

# 10. Rejoin tokens into a clean text
cleaned_text = ' '.join(tokens_filtered)
print("\n10. Final Cleaned Text:")
print(cleaned_text)

import nltk
from nltk.util import ngrams
from nltk.corpus import words
from difflib import get_close_matches

# Download English words corpus (if not already downloaded)
nltk.download('words')

# Load dictionary of English words
word_list = set(words.words())

def generate_ngrams(word, n=2):
    """Generate n-grams for a given word"""
    return [''.join(gram) for gram in ngrams(word, n)]

def suggest_correction(misspelled_word, n=2):
    """Suggest correct words based on n-gram similarity"""
    misspelled_ngrams = set(generate_ngrams(misspelled_word, n))
    suggestions = {}

    for correct_word in word_list:
        correct_ngrams = set(generate_ngrams(correct_word, n))
        similarity = len(misspelled_ngrams & correct_ngrams) / max(len(misspelled_ngrams), len(correct_ngrams))
        suggestions[correct_word] = similarity

    # Get top 3 suggestions
    sorted_suggestions = sorted(suggestions, key=suggestions.get, reverse=True)[:3]
    return sorted_suggestions

# Example usage
misspelled = input("Enter a misspelled word: ")
corrections = suggest_correction(misspelled, n=3)

if corrections:
    print(f"Did you mean: {', '.join(corrections)}?")
else:
    print("No suggestions found.")

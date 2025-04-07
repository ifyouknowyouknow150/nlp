pip install nltk
from nltk import CFG, ChartParser
import re

# Step 1: Define the Grammar with Extended Rules
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det Adj N | Det N PP
VP -> V NP | V PP | V
PP -> P NP
Det -> 'the' | 'a' | 'an'
N -> 'cat' | 'dog' | 'ball' | 'park' | 'game' | 'man' | 'woman'
Adj -> 'big' | 'small' | 'beautiful' | 'lazy' | 'fast'
V -> 'chased' | 'saw' | 'kicked' | 'played' | 'ran' | 'jumped'
P -> 'in' | 'on' | 'by' | 'with'
""")

# Step 2: Create the parser
parser = ChartParser(grammar)

# Step 3: Take user input
sentence = input("Enter a sentence: ").strip()

# Function to suggest basic corrections for common errors
def suggest_corrections(sentence):
    suggestions = []

    # Basic checks for missing parts of speech
    words = sentence.split()

    if len(words) < 2:
        suggestions.append("The sentence seems too short. Try adding more words.")

    if re.search(r'\s(the|a|an)\s$', sentence):
        suggestions.append("The sentence ends with an article, but lacks a noun after it.")

    if re.search(r'[\w]+$', sentence) and not any(word in words for word in ['chased', 'saw', 'kicked', 'played', 'ran', 'jumped']):
        suggestions.append("The sentence seems to lack a verb. Try adding an action verb.")

    return suggestions

# Step 4: Parse the sentence
try:
    parses = list(parser.parse(sentence.split()))
    if parses:
        print("The sentence is grammatically correct!")
        print("Parse Trees:")
        for tree in parses:
            tree.pretty_print()
    else:
        print("The sentence is not grammatically correct.")
        corrections = suggest_corrections(sentence)
        if corrections:
            print("Suggestions for correction:")
            for suggestion in corrections:
                print(f"- {suggestion}")
        else:
            print("No suggestions available, please check the grammar.")
except ValueError as e:
    print("Error:", e)

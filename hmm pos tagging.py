import nltk
from nltk.corpus import treebank
from nltk.tag import hmm
from sklearn.model_selection import train_test_split

# Download necessary data
nltk.download('treebank')
nltk.download('universal_tagset')

# Load the dataset
data = treebank.tagged_sents(tagset='universal')

# Split into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Train the HMM tagger
trainer = hmm.HiddenMarkovModelTrainer()
tag_model = trainer.train(train_data)


# Predict and evaluate
def evaluate_hmm(tagger, test_data):
    accuracy = tagger.evaluate(test_data)
    return accuracy


# Example usage
if __name__ == "__main__":
    accuracy = evaluate_hmm(tag_model, test_data)
    print(f"HMM POS Tagger Accuracy: {accuracy:.4f}")

    # Test on a sample sentence
    sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    predicted_tags = tag_model.tag(sentence)
    print("POS Tags:", predicted_tags)

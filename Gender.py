import nltk
import random
from nltk.corpus import names
from nltk.classify import apply_features

# Download dataset if not already downloaded
nltk.download('names')

# Load name dataset
male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]

# Combine and shuffle the dataset
labeled_names = male_names + female_names
random.shuffle(labeled_names)

# Feature extractor: last letter of the name
def gender_features(name):
    return {
        'last_letter': name[-1].lower()
    }

# Create feature sets
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]

# Split into training and testing data
train_set = featuresets[:5000]
test_set = featuresets[5000:]

# Train a Naive Bayes classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Test accuracy
print("Accuracy:", nltk.classify.accuracy(classifier, test_set))

# Show most informative features
classifier.show_most_informative_features(5)

# Predict gender for new names
def predict_gender(name):
    gender = classifier.classify(gender_features(name))
    print(f"Name: {name} → Predicted Gender: {gender}")

# Test predictions
predict_gender("Prem")
predict_gender("nivati")
predict_gender("Navya")
predict_gender("Arpan")

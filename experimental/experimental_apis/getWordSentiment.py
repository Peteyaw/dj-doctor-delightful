### IMPORTS

from textblob import TextBlob


### FUNCTIONS

def getSemtimentsGivenText(text):

	blob = TextBlob(text)
	sentences = blob.sentences
	sentiments = []

	for sentence in sentences:
		sentiments.append(sentence.sentiment.polarity)

	return sentiments

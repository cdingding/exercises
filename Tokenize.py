import re
import string
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

PUNCTUATION = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))

def tokenize(text):
  regex = re.compile('<.+?>|[^a-zA-Z]')
  clean_txt = regex.sub(' ', text)
  tokens = clean_txt.split()
  lowercased = [t.lower() for t in tokens]

  no_punctuation = []
  for word in lowercased:
      punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])
      no_punctuation.append(punct_removed)
  no_stopwords = [w for w in no_punctuation if not w in STOPWORDS]

  STEMMER = PorterStemmer()
  stemmed = [STEMMER.stem(w) for w in no_stopwords]
  return [w for w in stemmed if w]

if __name__ == '__main__':
    text1 = ' Hello, I am Charlie. Who are better? a <book>? YOu know what 1+1 equals?'
    print tokenize(text1)
    print word_tokenize(text1)
    print text1.split()
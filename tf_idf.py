from collections import Counter
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from math import sqrt
import math

'''
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

word_lst = ['ding', 'ding', 'changsong', 'hello']
def get_tf(word_lst):
    count_of_each_word = Counter(word_lst)
    doc_word_count = len(word_lst) * 1.
    return np.array([count_of_each_word[v] / doc_word_count if v in count_of_each_word else 0 for v in vocab])
'''

doc1 = 'the cat in the hat?'
doc2 = 'the cat in the tree!'
doc3 = 'the cat ate my hat'
doc4 = 'the cat in the hat the cat in the hat the cat in the hat'

documents = [doc1, doc2, doc3, doc4]
#clean option 1
regex = re.compile('<.+?>|[^a-zA-Z]')
vocabulary = [regex.sub('', word) for doc in documents for word in doc.split()]

#clean option 2
vocabulary = [word.strip('?!') for doc in documents for word in doc.split()]

vocabulary = sorted(list(set(vocabulary)))
print vocabulary

print 'Vocabulary (features):',vocabulary

def vectorize(doc, vocabulary):
    bag_of_words = Counter(doc.split(' '))
    doc_vector = np.zeros(len(vocabulary))
    for word_index, word in enumerate(vocabulary):
        if word in bag_of_words:
            doc_vector[word_index] += bag_of_words[word]
    return doc_vector
print Counter([word.strip('?!') for word in doc1.split(' ')])

doc1 = 'the cat in the hat'
doc2 = 'the cat in the tree'
doc3 = 'the cat ate my hat'
doc4 = 'the cat in the hat the cat in the hat the cat in the hat'
documents = [doc1, doc2, doc3, doc4]

def vectorize(doc, vocabulary):
    bag_of_words = Counter(doc.split(' '))
    # print Counter(doc.split())
    doc_vector = np.zeros(len(vocabulary))
    for word_index, word in enumerate(vocabulary):
        if word in bag_of_words:
            doc_vector[word_index] += bag_of_words[word]
    print 'doc_vector is: ', doc_vector
    return doc_vector

doc1_vectorized = vectorize(doc1, vocabulary)
print doc1_vectorized
def vectorized(docs, vocabulary):
    docV = []
    for i, doc in enumerate(docs):
        docV.append(vectorize(doc, vocabulary).reshape(1,-1))
    tf_matrix = np.vstack(docV)
    return tf_matrix

tf_matrix = vectorized(documents, vocabulary)
print 'function tf_matrix: \n', tf_matrix


# doc1_vectorized = vectorize(doc1, vocabulary).reshape(1, -1)
# doc2_vectorized = vectorize(doc2, vocabulary).reshape(1, -1)
# doc3_vectorized = vectorize(doc3, vocabulary).reshape(1, -1)
# doc4_vectorized = vectorize(doc4, vocabulary).reshape(1, -1)

doc1_vectorized = vectorize(doc1, vocabulary)
doc2_vectorized = vectorize(doc2, vocabulary)
doc3_vectorized = vectorize(doc3, vocabulary)
doc4_vectorized = vectorize(doc4, vocabulary)

print 'doc1_vectorized by reshape(-1,1): \n', doc1_vectorized

tf_matrix = np.vstack((doc1_vectorized,
                       doc2_vectorized,
                       doc3_vectorized,
                       doc4_vectorized))
print 'manual tf_matrix: \n',tf_matrix
print 'type(tf_matrix by np.vstack: \n', type(tf_matrix)

tf_matrix1 = np.array([doc1_vectorized, \
                       doc2_vectorized,\
                       doc3_vectorized ,\
                       doc4_vectorized ])
print 'tf_matix by assemple: \n', tf_matrix1

print 'SKlearn results----------------'
count_vectorizer = CountVectorizer(stop_words=None, vocabulary = vocabulary)
feature_matrix =count_vectorizer.fit_transform([doc1]).todense()

print feature_matrix
print 'our result',vectorize(doc1, vocabulary)
print 'Compare "%s" \nwith "%s"'%(doc1, doc2)
print doc1_vectorized, doc3_vectorized
print 'view ------'
# doc1_vectorized = doc1_vectorized
# doc3_vectorized = doc3_vectorized
# doc1_vectorized = doc1_vectorized.reshape(-1,1)
# doc3_vectorized = doc3_vectorized.reshape(-1,1)
x_x = doc1_vectorized-doc3_vectorized
distance = sqrt(np.sum(x_x**2)) # Or use np.sum() if not reshape(-1,1)
print '\ncalculated distance: ', distance
print euclidean_distances(doc1_vectorized, doc3_vectorized)
print '\nCompare "%s" \nwith "%s"'%(doc1, doc4)
print 'doc 1 vectorized: ', doc1_vectorized
print 'doc 3 vectorized: ', doc3_vectorized
print 'sklearn cosine similarity is: \n'
print cosine_similarity(doc1_vectorized, doc3_vectorized)

print '\nConsine ---------------'
def my_cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumyy, sumxy = 0, 0, 0
    for i in range(len(v1)):
        sumxx += v1[i] ** 2
        print sumxx, v1[i]
        sumyy += v2[i] ** 2
        sumxy += v1[i] * v2[i]
    # print sumxx
    # print sumyy
    # print sumxy
    return 1.0 * sumxy / sqrt(sumxx * sumyy)

def my_cosine_similarity1(v1,v2):
    return np.dot(v1,v2) / sqrt(np.dot(v1,v1) * np.dot(v2,v2))

doc1_vectorized = vectorize(doc1, vocabulary)
doc2_vectorized = vectorize(doc2, vocabulary)
doc3_vectorized = vectorize(doc3, vocabulary)
doc4_vectorized = vectorize(doc4, vocabulary)

print my_cosine_similarity(doc1_vectorized, doc2_vectorized)

# examples
v1,v2 = [3, 45, 7, 2], [2, 54, 13, 15]
print my_cosine_similarity(v1, v2)
print my_cosine_similarity1(v1, v2)
print cosine_similarity(v1, v2)

print euclidean_distances(v1,v2)
print sqrt(sum((np.array(v1)-np.array(v2))**2))

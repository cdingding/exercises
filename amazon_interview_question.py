'''
1. input of model (tf-idf vectors)
2. steps before input (tokenize, remove stopwords, remove punctuations, tf-idf vectorize)
3. what other models besides multiclassification (Logistic, RF, GBRT)
4. Assemble and how to predict better (use the one with most votes)
5. matrix for W letter, count the black pixels
6. find the # of neighbors who are white pixels of black
'''

import numpy as np

def count_black(mat):
    return np.sum(mat)

def find_white1(pixels): #input black pixels
    white_num =0
    for i in range(len(pixels)):
        for j in range(len(pixels)):
            if pixels[i][j] == 1:
                if i>0 and i < len(pixels) and j > 0 and j < len(pixels) and pixels[i][j-1]==0:
                    white_num += 0
                if i>0 and i < len(pixels) and j > 0 and j < len(pixels) and pixels[i][j+1]==0:
                    white_num += 0
                if i>0 and i < len(pixels) and j > 0 and j < len(pixels) and pixels[i-1][j] == 0:
                    white_num += 0
                if i>0 and i < len(pixels) and j > 0 and j < len(pixels) and pixels[i-1][j] == 0:
                    white_num += 0
    return white_num

def find_white_neighbors(pixels): #input black pixels
    white_num =0
    for i in range(len(pixels)):
        for j in range(len(pixels)):
            if pixels[i][j] == 1:
                if i > 0 and i < len(pixels)-1 and j > 0 and j < len(pixels)-1 and pixels[i][j-1] == 0:
                    white_num += 1
                if i > 0 and i < len(pixels)-1 and j > 0 and j < len(pixels)-1 and pixels[i][j+1] == 0:
                    white_num += 1
                if i > 0 and i < len(pixels)-1 and j > 0 and j < len(pixels)-1 and pixels[i-1][j] == 0:
                    white_num += 1
                if i > 0 and i < len(pixels)-1 and j > 0 and j < len(pixels)-1 and pixels[i-1][j] == 0:
                    white_num += 1
    return white_num

def find_white_neighbors(pixels): #input black pixels
    white_num =0
    for i in range(1,len(pixels)-1):
        for j in range(1,len(pixels)-1):
            if pixels[i][j] == 1:
                if pixels[i][j-1] == 0:
                    white_num += 1
                if pixels[i][j+1] == 0:
                    white_num += 1
                if pixels[i-1][j] == 0:
                    white_num += 1
                if pixels[i-1][j] == 0:
                    white_num += 1
    return white_num

if __name__ == '__main__':
    mat = [[1,0,1,1], [0,1,0,1], [0,0,1,1], [1,1,1,1]]
    print count_black(mat)
    print find_white(mat)
    print find_white2(mat)
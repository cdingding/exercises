import numpy as np


def roc_curve(probabilities, labels):
    '''
    INPUT: numpy array, numpy array
    OUTPUT: list, list, list
    Take a numpy array of the predicted probabilities and a numpy array of the
    true labels.
    Return the True Positive Rates, False Positive Rates and Thresholds for the
    ROC curve.
    '''

    thresholds = np.sort(probabilities)

    tprs = []
    fprs = []

    num_positive_cases = sum(labels)
    num_negative_cases = len(labels) - num_positive_cases

    for threshold in thresholds:
        # With this threshold, give the prediction of each instance
        predicted_positive = probabilities >= threshold
        # Calculate the number of correctly predicted positive cases
        true_positives = np.sum(predicted_positive * labels)
        # Calculate the number of incorrectly predicted positive cases
        false_positives = np.sum(predicted_positive) - true_positives
        # Calculate the True Positive Rate
        tpr = true_positives / float(num_positive_cases)
        # Calculate the False Positive Rate
        fpr = false_positives / float(num_negative_cases)

        fprs.append(fpr)
        tprs.append(tpr)

    return tprs, fprs, thresholds.tolist()

if __name__ == '__main__':
    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.cross_validation import train_test_split

    # y1 = [2,2,1,2,1,2,1,2]
    y1 = [1,1,0,1,0,1,0,1]
    scores1 = [0.9,0.8,0.75,0.7,0.5,0.3,0.2,0.1]
    # y2 = [2,2,1,2,1,2,1,1]
    y2 = [1, 1, 0, 1, 0, 1, 0, 0]
    scores2 = [0.9,0.8,0.75,0.7,0.5,0.3,0.2,0.1]
    # y3 = [2,2,1,2,1,1,1,1]
    y3 = [1,1,0,1,0,0,0,0]
    scores3 = [0.9,0.8,0.75,0.7,0.5,0.3,0.2,0.1]

    tpr, fpr, thresholds = roc_curve(scores1, y1)

    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Sensitivity, Recall)")
    plt.title("ROC plot of loan data")
    plt.show()
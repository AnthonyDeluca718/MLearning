import numpy as np

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def perceptron(data, ans, alpha, max_iter):
    w = np.zeros(len(ans))


data = np.matrix('[2, -2; 0.8, 3; 0.5, 3; 1.7, 1; 0.5, 3; 1.05, -1; .95, -1]')
ans = [1, -1, 1, -1, 1, -1] # correct answers

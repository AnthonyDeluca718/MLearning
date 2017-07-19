import numpy as np

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

data = [
    {
        'z': 1,
        'x': np.matrix('[.25; -1]')
    },
    {
        'z': -1,
        'x': np.matrix('[-1,;.1]')
    },
    {
        'z': 1,
        'x': np.matrix('[.1,;1]')
    },
    {
        'z': -1,
        'x': np.matrix('[-.2; 3]')
    }
]

# for d in data:
#     print(d['z'])
#     print(d['x'])

def perceptron(w = np.matrix('[0.0;0.0]'), data = [], alpha = 0.1, n_iter = 1):

    for i in range(n_iter):
        for d in data:
            diff = d['z'] - sign(np.dot(w.transpose(),d['x']))
            w = w + alpha*diff*d['x']
    return w

w_star = perceptron(np.matrix('[0;0]'), data, 0.1, 5)

for d in data:
    predicted = sign(np.dot(w_star.transpose(), d['x']))
    print('True: ' + str(d['z']) + '. Predicted: ' + str(predicted) )

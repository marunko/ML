import numpy as np

# One layer Neural net simulation
def oneLayer():
    #INPUT_X = [1.0, 2.0, 3.0, 2.5]
    INPUT_X = [[1.0, 2.0, 3.0, 2.5],
               [1.0, 2.0, 3.0, 2.5],
               [1.0, 2.0, 3.0, 2.5]]
    # unique weights for each 3 neurons and same 4 inputs layers

    Weights = [[3.1, 2.1, 8.7, 1.1],
               [3.1, 2.1, 8.7, 1.1],
               [3.1, 2.1, 8.7, 1.1]]
    biases = [2,3,0.5]
    Weights2 = [[3.1, 2.1, 8.7],
               [3.1, 2.1, 8.7],
               [3.1, 2.1, 8.7]]
    biases2 = [2, 3, 0.5]

#transpose matrix Weights
    input_X_Layer2 = np.dot(INPUT_X, np.array(Weights).T)+biases
    print(input_X_Layer2)

    output = np.dot(input_X_Layer2, np.array(Weights2).T)+biases2
    print(output)
#multiple layers

def fullnet():
    input_vector = np.array([1.66, 1.56])
    weights_1 = np.array([1.45, -0.66])
    bias = np.array([0.0])
    layer_1 = np.dot(input_vector, weights_1) + bias
    layer_2 = sigmoid(layer_1)
    print(layer_1)
    print(layer_2)
    return layer_2


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

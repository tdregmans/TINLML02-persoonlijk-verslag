"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-05-09 (YYYY-MM-DD)
    Version: 5.0

"""

import numpy as np
import NeuralNetwork

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

nn = NeuralNetwork.NeuralNetwork(input_size=2, hidden_size=4, output_size=1)
nn.train(X, y, epochs=10000, learning_rate=0.1)

# Test the trained model
output = nn.feedforward(X)
print("Predictions after training:")
print(output)

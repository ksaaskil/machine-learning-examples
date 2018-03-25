from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
import math

# 1D linear regression example

hidden_slope = 2.0
hidden_bias = 5.0

hidden_model = lambda x: hidden_slope*x + hidden_bias

samples = 100
features = 1

# X = np.resize(np.linspace(1, samples, samples), (samples, features))
X = np.linspace(1, samples, samples)
X.resize((samples, 1))
print('X shape: (%d, %d)' % X.shape)

noise_std = 10
# Alternative way to resize
Y = hidden_model(X) + np.random.randn(X.shape[0], X.shape[1]) * noise_std
Y = np.resize(Y, (samples, 1))
print('Y shape: (%d, %d)' % Y.shape)

model = Sequential()
nodes = 1
model.add(Dense(nodes, activation='linear', input_dim = features))

# Scale data to help optimizer
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
sc_Y = StandardScaler()
Y = sc_Y.fit_transform(Y)

# Split to training and validation sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.10, random_state = 42)

# --------------
# Pick optimizer
# optimizer = 'rmsprop'
# optimizer = optimizers.RMSprop()
optimizer = optimizers.SGD(lr = 0.01)
# optimizer = optimizers.Adam()

# --------------
# Pick loss function
# loss = 'mean_squared_error'

# Mean squared error explicitly
import keras.backend as K
def mse_loss(y_true, y_pred):
    return K.mean(K.square(y_pred - y_true), axis=-1)

loss = mse_loss

# ---------------
# Compile
model.compile(optimizer = optimizer, loss = loss, metrics = ['mse'])

# Initial values
# model.set_weights([np.array([[2.5]]), np.array([4.0])])

# Train
model.fit(X_train, Y_train, epochs = 200, verbose = 1)

print('Got weights:')
print(model.get_weights())

# params = model.get_weights()

# print('Evaluate:')
# print(model.evaluate(sc_X.inverse_transform(X_test), sc_Y.inverse_transform(Y_test)))
# model.summary()

Y_predicted = model.predict(X)

from keras.datasets import imdb
from keras.preprocessing import sequence

from keras import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout

vocabulary_size = 50000

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words = vocabulary_size)
print('Loaded data with {} training samples and {} test samples'.format(len(X_train), len(X_test)))

#padding sequences
max_words = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)

embedding_size = 32
model = Sequential()
model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

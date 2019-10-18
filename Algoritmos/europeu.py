import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasRegressor
import matplotlib.pyplot as plt

base = pd.read_excel('europeu.xlsx', encoding='ISO-8859-1')

previsores = base.iloc[:,0:15].values
profundidade = base.iloc[:,15:16].values

from sklearn.model_selection import train_test_split
previsores_treinamento,previsores_teste,profundidade_treinamento,profundidade_teste=train_test_split(previsores,profundidade,test_size=0.2)

regressor = Sequential()
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal',input_dim=15))
regressor.add(Dropout(0.3))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.3))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.3))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.3))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.3))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.3))
regressor.add(Dense(units=1,activation='linear'))
regressor.compile(loss='mean_absolute_error',optimizer='adam',
                  metrics = ['mean_absolute_error'])
model = regressor.fit(previsores_treinamento,profundidade_treinamento,batch_size=100,
                      epochs=5000,validation_data=(previsores_teste,profundidade_teste))

previsoes = regressor.predict(previsores_teste)
resultado = regressor.evaluate(previsores_teste,profundidade_teste)

# Get training and test loss histories
training_loss = model.history['loss']
test_loss = model.history['val_loss']

# Create count of the number of epochs
epoch_count = range(1, len(previsoes) + 1)

plt.plot(epoch_count, profundidade_teste, 'r--')
plt.plot(epoch_count, previsoes, 'b-')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show();



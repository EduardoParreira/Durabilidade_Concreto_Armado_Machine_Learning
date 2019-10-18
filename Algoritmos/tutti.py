import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasRegressor
import matplotlib.pyplot as plt

base = pd.read_excel('tutti.xlsx', encoding='ISO-8859-1')

previsores = base.iloc[:,0:2].values
profundidade = base.iloc[:,2:3].values

from sklearn.model_selection import train_test_split
previsores_treinamento,previsores_teste,profundidade_treinamento,profundidade_teste=train_test_split(previsores,profundidade,test_size=0.2)

regressor = Sequential()
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal',input_dim=2))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=32, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=48, activation='linear',kernel_initializer='normal'))
regressor.add(Dropout(0.2))
regressor.add(Dense(units=1,activation='linear'))
regressor.compile(loss='mean_absolute_error',optimizer='adam',
                  metrics = ['mean_absolute_error'])
model = regressor.fit(previsores_treinamento,profundidade_treinamento,batch_size=100,
                      epochs=5000,validation_data=(previsores_teste,profundidade_teste))

previsoes = regressor.predict(previsores_teste)
resultado = regressor.evaluate(previsores_teste,profundidade_teste)

training_loss = model.history['loss']
test_loss = model.history['val_loss']

epoch_count = range(1, len(training_loss) + 1)

plt.plot(epoch_count, training_loss, 'r--')
plt.plot(epoch_count, test_loss, 'b-')
plt.legend(['Training Loss', 'Test Loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show();



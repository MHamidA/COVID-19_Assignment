import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Bidirectional, Dropout
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from datetime import date

class CovidDeathsForecast:
    def __init__(self, file_path, variable = "total_deaths", iso_code = 'FRA', time_step = 7):
        self.file_path = file_path
        self.variable = variable
        self.iso_code = iso_code
        self.time_step = time_step
    def createDataset(self, dataset, time_step=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-time_step):
            dataX.append(dataset[i:(i+time_step)])
            dataY.append(dataset[i + time_step])
        return np.array(dataX), np.array(dataY)
    def multi_step_forecasts(self, n_past, n_future):
        x_past = self.X_val[- n_past - 1:, :, :][:1] 
        y_past = self.y_val[- n_past - 1]            
        y_future = []                      
        for i in range(n_past + n_future):
            x_past = np.append(x_past[:, 1:, :], y_past.reshape(1, 1, 1), axis=1)
            y_past = self.model.predict(x_past)
            y_future.append(y_past.flatten()[0])
        y_future = self.scaler.inverse_transform(np.array(y_future).reshape(-1, 1)).flatten()
        return y_future
    def fit_transform(self):
        data_raw = pd.read_csv(self.file_path)
        data_country = data_raw.loc[data_raw['iso_code'] == self.iso_code]
        country_data = data_country.reset_index().loc[:, ['date', self.variable]]
        country_data[self.variable] = country_data[self.variable].fillna(0)
        country_data['date'] = pd.to_datetime(country_data['date'])
        datalen = len(country_data)
        datainp = country_data[self.variable].values.reshape(datalen,1)
        self.scaler = MinMaxScaler(feature_range=(0,1))
        scaleddatainp = self.scaler.fit_transform(datainp)
        train_split = .85
        train_size = int(train_split * datalen)
        self.trainData = scaleddatainp[:train_size]
        self.valData = scaleddatainp[train_size:]
        self.X_train,self.y_train = self.createDataset(self.trainData, time_step=self.time_step)
        self.X_val,self.y_val = self.createDataset(self.valData, time_step=self.time_step)
        self.model = Sequential()
        self.model.add(Bidirectional(layers.LSTM(256, activation='relu'), input_shape=[self.time_step, 1]))
        self.model.add(Dropout(0.5))
        self.model.add(layers.Dense(1))
        self.model.summary()
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.history = self.model.fit(self.X_train, self.y_train, epochs=100, batch_size=32, validation_data=(self.X_val, self.y_val), verbose=1, shuffle=False, callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)])
    def save_model(self,model_name):
        self.model.save(model_name)
    def evaluate_model(self):
        self.model.evaluate(self.X_val,self.y_val)
    def predict_train_val(self):
        self.y_train_hat = self.scaler.inverse_transform(self.model.predict(self.X_train))
        self.y_val_hat = self.scaler.inverse_transform(self.model.predict(self.X_val))
    def forecast(self, n_future, end_date):
        d0 = date(end_date.year, 1, 16)
        d1 = date(2023, 3, 31)
        delta = d1 - d0
        print("Forecasting untill the end of March")
        self.forecast_1 = self.multi_step_forecasts(n_past=0,        n_future=delta.days)
        new_dates = pd.date_range(start='2023-01-17', end='2023-03-31', freq='D')
        self.forecasted_data = pd.DataFrame({'date': new_dates, self.variable: self.forecast_1})
    def save_forecast(self, csv_name):
        self.forecasted_data.to_csv(csv_name, index = False)
        print("Forecast data saved as ",csv_name)

if __name__ == '__main__':
    forecast = CovidDeathsForecast(file_path='Assets/owid-covid-data.csv', iso_code='FRA', variable='total_deaths', time_step=7)
    forecast.fit_transform()
    forecast.save_model('model1_totaldeaths.h5')
    forecast.evaluate_model()
    forecast.predict_train_val()
    forecast.forecast(74, date(2023,1,16))
    forecast.save_forecast('tdeaths_forecasted.csv')
    print("DONE!!!")



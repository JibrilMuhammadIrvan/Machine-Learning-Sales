import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Muat dataset
data_file = "C:\\Python\\Machine Learning\\Data Penjualan Paskal\\data_penjualan.csv"
df = pd.read_csv(data_file)

# Praproses data
df['tanggal'] = pd.to_datetime(df['tanggal'], format="%d/%m/%Y")
df['ordinal_tanggal'] = df['tanggal'].apply(lambda x: x.toordinal())

# Bagi data menjadi data latih dan data uji
X = df['ordinal_tanggal'].values.reshape(-1, 1)
y = df['penjualan'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pilih dan latih model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: ", rmse)

# Visualisasikan prediksi
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.scatter(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Tanggal (ordinal)')
plt.ylabel('Penjualan')
plt.legend()
plt.show()

# Gunakan model untuk membuat prediksi pen jualan di masa depan
future_date = pd.to_datetime("2023-05-12", format="%Y-%m-%d")
ordinal_future_date = future_date.toordinal()
future_sales = model.predict([[ordinal_future_date]])
print("Prediksi penjualan pada {}: {}".format(future_date.strftime("%d-%m-%Y"), future_sales[0]))

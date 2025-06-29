from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Data
data = {'Experience': [1,2,3,4,5], 'Salary': [300,350,500,550,600]}
df = pd.DataFrame(data)

# Split the data into training and testing sets
x = df[['Experience']]
y = df['Salary']

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2)

model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)

print("Predictions: ", predictions)
print("Mean Squared Error: ", mean_squared_error(y_test, predictions))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")
df.dropna(inplace=True)
x = df[["Distances","Flight_time"]]
y = df[["Price"]]
x_train, x_test, y_train, y_test = train_test_split(x.values, y.values, train_size = 0.5, test_size = 0.5, random_state=1)
regression = LinearRegression()
regression.fit(x_train,y_train)


#predicting airport
df2 = pd.read_csv("data2.csv")
a = [[72.27 ,0.1117145073700545]]
print(regression.predict(a))




import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("premstats.csv")
print(df.describe())
print(df.columns)
y = df.Points
X = df.Value
X = X.values.reshape(-1, 1)
y = y.values.reshape(-1, 1)

#Making our Linear Regression Model
model = LinearRegression()
model.fit(X,y)
predictions = model.predict(X)

#Plotting a graph
plt.scatter(X, y, alpha=0.4)
plt.plot(X,predictions, "-")
plt.title("Premier League")
plt.xlabel("Team Values from seaons 2013/14 to 2018/19")
print(model.score(X, y))

plt.ylabel("Points collected")
plt.show()

print('\n')

while True:
    enquiry = float(input("Enter the value of a team, and I'll predict the number of points they'll collect!"))
    print(int(model.predict([[enquiry]])))
    print('\n \n')

import pandas as pd

xyz=pd.read_csv('hw.csv')
print(xyz.head(5))

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("hw.csv")

print(dataset)
x=dataset.iloc[: , :-1].values
X=dataset.iloc[: , :-1].values
y=dataset.iloc[: , 1].values
print(X)
print(y)

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X , y)


print("y= " + str(regressor.coef_) + "X + " + str(regressor.intercept_))

print("Accuracy:" , regressor.score(X , y) * 100)

plt.plot(X , y , 'o')
plt.plot(X , regressor.predict(X))
plt.show()
predict_x=int(input('Enter Height:'))
predict_y=(0.67461045 * predict_x) - 38.45508707607698
plt.scatter(X , y)
plt.scatter(predict_x , predict_y)
plt.xlabel('Enter Height:(Predicted_x)')
plt.ylabel('Enter Weight:(Predicted_y)')

plt.plot(X , regressor.predict(X) , color='green')
plt.show()

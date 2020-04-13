import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Load Data 
data = pd.read_csv("cars1.csv")

#Plot Data
X = data["Weight"]
y = data["Horsepower"]


# x = np.linspace(1.0, 33, num=5000)

# why = 0 +6*x
# plt.plot(why)

plt.scatter(X, y)
plt.show()



step_size = 0.0001


# print(X[0])

# print(sum(1*X-y))


def gradientDescent(X,y,a,m):

    theta1 = 10000
    theta0 = 10000
    for l in range(1,10):
        sum0 = 0
        sum = 0

        for i in range(0,m):
            sum0 += theta0 - (theta1*X[i]-y[i])


        for i in range(0,m):
            sum += theta1 - (theta1*X[i]-y[i])*X[i]

        temp0 = (a/m)*sum0
        temp = (a/m)*sum
        theta0 = temp0
        theta1 = temp
    
    return [theta0, theta1]

       

#     return [theta0, theta1]
        
# cost = []

# for i in range(1,1000):
    
#     theta1 = 1
#     X_transpose = X.transpose()
#     gradient = step_size/406 * sum((theta1*X-y)*X_transpose)

#     print(gradient)
    




print(gradientDescent(X,y,step_size,406))





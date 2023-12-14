import numpy as np
import pandas
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm



data=pd.read_csv("D:\LAP_TRINH\PYTHON\PYTHON_8\MNM\THUC_HANH\Student_Performance.csv")
data.head()


X=data["Hours Studied"]
Y=data["Performance Index"]


x_train,x_test,y_train,y_test=train_test_split(X,Y,train_size = 0.8,test_size = 0.2,random_state =100 )

plt.scatter(x_train, y_train)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

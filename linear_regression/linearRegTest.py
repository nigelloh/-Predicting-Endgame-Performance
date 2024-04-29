import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression


def linearRegTest(df, testdf, features):
    print('\n===Linear Reg Test===')
    y_COL = 'gold_earned'
    X_train = df[features]
    y_train = df[y_COL]
    X_test = testdf[features]
    y_test = testdf[y_COL]

    lm = LinearRegression()
    lm.fit(X_train, y_train)


    # get all the performance metrics
    y_pred = lm.predict(X_test)
    r2 = lm.score(X_test, y_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    print('R²:', r2)
    print('Mean Squared Error:', mse)
    print('Root Mean Squared Error:', rmse)
    print('Mean Absolute Error:', mae)
    print(f'Mean Absolute Percent Error: {mape}%')

    # plot linear regression graph
    plt.scatter(y_test, y_pred, alpha=0.3)
    plt.title('Linear Regression (Predict Total)')
    plt.xlabel('Actual Value')
    plt.ylabel('Predicted Value')
    plt.savefig('linearReg_Test.png')
    plt.close()

    # plot residuals
    residuals = y_test - y_pred
    plt.scatter(y_pred, residuals, alpha=0.3)
    # plot the 0 line (we want our residuals close to 0)
    plt.plot([min(y_pred), max(y_pred)], [0, 0], color='red')
    plt.title('Residual Plot 1')
    plt.xlabel('Fitted')
    plt.ylabel('Residual')
    plt.savefig('Residual_Graph_Test.png')
    plt.close()

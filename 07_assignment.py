'''
Assignment #7

1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not 
    guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 07_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables unless stated to do so
7. Make sure your work is committed to your master branch in Github


Packages required:

pip install cloudpickle==0.5.6 (this is an optional install to help remove a deprecation warning message from sklearn)
pip install sklearn
pip install websockets

Optional:
pip install python-binance

'''
# core
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import websockets as ws
import asyncio
from binance.websockets import BinanceSocketManager
from binance.client import Client
import time

# ml
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts

# infra
import unittest

# ------ Place code below here \/ \/ \/ ------
# import plotly library and enter credential info here

import chart_studio

import chart_studio.plotly as py
import plotly.graph_objects as go


#set credentials for plotly api
chart_studio.tools.set_credentials_file(username='ilawl', api_key='x0xhOzxAG3ESuEUumQH0')

# ------ Place code above here /\ /\ /\ ------





# ------ Place code below here \/ \/ \/ ------
# Load datasets here once and assign to variables iris and boston

#loads iris data from datasets
iris = ds.load_iris()

#saves iris data into a dataframe and renames columns accordingly
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris.feature_names

#creates list for iris target values
iris_target = [str(item) for item in iris.target]

#changes target values to the target names
for n, i in enumerate(iris_target):
    
    if i == "0":
        iris_target[n] = iris.target_names[0]
        
    elif i == "1":
        iris_target[n] = iris.target_names[1]
        
    elif i == "2":
        iris_target[n] = iris.target_names[2]
        
    else:
        iris_target[n] = "Unknown"


#loads boston dataset
boston = ds.load_boston()

#saves data as a dataframe and renames the columns
boston_df = pd.DataFrame(boston.data)
boston_df.columns = boston.feature_names

#saves boston target values
boston_target = boston.target

# ------ Place code above here /\ /\ /\ ------




# 10 points
def exercise01():
    '''
        Data set: Iris
        Return the first 5 rows of the data including the feature names as column headings in a DataFrame and a
        separate Python list containing target names
    '''

    # ------ Place code below here \/ \/ \/ ------

    #saves iris data to pandas dataframe and renames columns
    iris_df = pd.DataFrame(iris.data)
    iris_df.columns = iris.feature_names

    #displays first five rows of the dataframe
    df_first_five_rows = iris_df.head(n=5)
    
    #creates list of target names
    target_names = iris.target_names

    # ------ Place code above here /\ /\ /\ ------


    return df_first_five_rows, target_names

# 15 points
def exercise02(new_observations):
    '''
        Data set: Iris
        Fit the Iris dataset into a kNN model with neighbors=5 and predict the category of observations passed in 
        argument new_observations. Return back the target names of each prediction (and not their encoded values,
        i.e. return setosa instead of 0).
    '''

    # ------ Place code below here \/ \/ \/ ------

    #creates iris dataframe
    iris_df = pd.DataFrame(iris.data)
    iris_df.columns = iris.feature_names
    
    #creates list of target values as strings
    iris_target = [str(item) for item in iris.target]
    
    #renames target values to their actual names
    for n, i in enumerate(iris_target):
        
        if i == "0":
            iris_target[n] = iris.target_names[0]
            
        elif i == "1":
            iris_target[n] = iris.target_names[1]
            
        elif i == "2":
            iris_target[n] = iris.target_names[2]
            
        else:
            iris_target[n] = "Unknown"
    
    #initializes knn with 5 neighbors
    knn = KNN(n_neighbors = 5)
    
    #fits knn to data
    knn.fit(iris_df,iris_target)
    
    #makes prediction from observations given
    iris_predictions = knn.predict(new_observations)
    


    # ------ Place code above here /\ /\ /\ ------


    return iris_predictions

# 15 points
def exercise03(neighbors,split):
    '''
        Data set: Iris
        Split the Iris dataset into a train / test model with the split ratio between the two established by 
        the function parameter split.
        Fit KNN with the training data with number of neighbors equal to the function parameter neighbors
        Generate and return back an accuracy score using the test data was split out

    '''
    random_state = 21

    

    # ------ Place code below here \/ \/ \/ ------

    #splits train and test data
    X_train, X_test, y_train, y_test = tts(iris_df,iris_target,test_size = split,random_state = random_state, stratify = iris_target)
    
    #initializes knn with number of neighbors specified from input
    knn = KNN(n_neighbors = neighbors)
    
    #fits data from training data
    knn.fit(X_train,y_train)
    
    #generates score on test data
    knn_score = knn.score(X_test,y_test)
    

    # ------ Place code above here /\ /\ /\ ------


    return knn_score

# 15 points
def exercise04():
    '''
        Data set: Iris
        Generate an overfitting / underfitting curve of kNN each of the testing and training accuracy performance scores series
        for a range of neighbor (k) values from 1 to 30 and plot the curves (number of neighbors is x-axis, performance score 
        is y-axis on the chart). Return back the plotly url.

    '''
    
    # ------ Place code below here \/ \/ \/ ------

    #splits training and testing data
    X_train, X_test, y_train, y_test = tts(iris_df,iris_target,test_size = 0.2,random_state = 21, stratify = iris_target)

    #creates an array of neighbors from 1 to 30
    neighbors = np.arange(1, 30)
    
    #creates empty lists to store train and test accuracy
    train_accuracy = np.empty(len(neighbors))
    test_accuracy = np.empty(len(neighbors))
    
    # Loop over different values of k
    for i, k in enumerate(neighbors):
        # Setup a k-NN Classifier with k neighbors: knn
        knn = KNN(n_neighbors = k)
    
        # Fit the classifier to the training data
        knn.fit(X_train,y_train)
        
        #Compute accuracy on the training set
        train_accuracy[i] = knn.score(X_train, y_train)
    
        #Compute accuracy on the testing set
        test_accuracy[i] = knn.score(X_test,y_test)

    #creates plotly figure object with neighbors as x and train and test accuracy as y
    fig = go.Figure(go.Scatter(x=neighbors, y=train_accuracy, mode='lines', name='Train Accuracy'))
    
    fig.add_trace(go.Scatter(x=neighbors, y =test_accuracy, mode = 'lines', name = 'Test Accuracy' ))
    
    #label figure
    fig.update_xaxes(title_text='Number of Neighbors')
    fig.update_yaxes(title_text='Accuracy')
    fig.update_layout(title = "Overfit Underfit Curve")
    
    #publishees the plot on plotly
    output = py.iplot(fig, filename='Overfit_Underfit_Curve')
    
    #fetches plot url from output
    plotly_overfit_underfit_curve_url = output.src
    

    # ------ Place code above here /\ /\ /\ ------


    return plotly_overfit_underfit_curve_url

# 10 points
def exercise05():
    '''
        Data set: Boston
        Load sklearn's Boston data into a DataFrame (only the data and feature_name as column names)
        Load sklearn's Boston target values into a separate DataFrame
        Return back the average of AGE, average of the target (median value of homes or MEDV), and the target as NumPy values 
    '''

    # ------ Place code below here \/ \/ \/ ------

    #load boston data into dataframe and renames columns
    boston_df = pd.DataFrame(boston.data)
    boston_df.columns = boston.feature_names

    #creates target list
    boston_target = boston.target
    
    #calculates average of age and average of target
    average_age = np.mean(boston_df.AGE)
    average_medv = np.mean(boston_target)
    
    #turns target list into a numpy array
    medv_as_numpy_values = np.array(boston_target)

    # ------ Place code above here /\ /\ /\ ------


    return average_age, average_medv, medv_as_numpy_values

# 10 points
def exercise06():
    '''
        Data set: Boston
        In the Boston dataset, the feature PTRATIO refers to pupil teacher ratio.
        Using a matplotlib scatter plot, plot MEDV median value of homes as y-axis and PTRATIO as x-axis
        Return back PTRATIO as a NumPy array
    '''

    # ------ Place code below here \/ \/ \/ ------

    #creates scatterplot of PTRATIO to medv
    plt.scatter(boston_df.PTRATIO,boston_target)
    plt.xlabel("Parent Teacher Ratio")
    plt.ylabel("Median Value of Homes")
    
    plt.show()
    
    #retypes ratio to numpy array
    X_ptratio = np.array(boston_df.PTRATIO)

    # ------ Place code above here /\ /\ /\ ------


    return X_ptratio

# 15 points
def exercise07():
    '''
        Data set: Boston
        Create a regression model for MEDV / PTRATIO and display a chart showing the regression line using matplotlib
        with a backdrop of a scatter plot of MEDV and PTRATIO from exercise06
        Use np.linspace() to generate prediction X values from min to max PTRATIO
        Return back the regression prediction space and regression predicted values
        Make sure to labels axes appropriately
    '''

    # ------ Place code below here \/ \/ \/ ------

    #creates linear regression object
    reg_model_fit = lm.LinearRegression()
    
    #creates training data
    X_train = np.array(boston_df.PTRATIO).reshape(-1,1)
    y_train = np.array(boston_target).reshape(-1,1)

    #fit model
    reg_model_fit.fit(X_train,y_train)
    
    #creates input values for prediction
    prediction_space = np.linspace(min(X_train),max(X_train)).reshape(-1,1)

    #predicts based off of input values
    reg_model = reg_model_fit.predict(prediction_space)
    
    #plot the scatter between PTRATIO and medv with regression line
    plt.scatter(boston_df.PTRATIO,boston_target)
    plt.plot(prediction_space,reg_model, color = "black",linewidth = 3)
    plt.xlabel("Parent Teacher Ratio")
    plt.ylabel("Median Value of Homes")
    plt.show()

    # ------ Place code above here /\ /\ /\ ------

    return reg_model, prediction_space

# 10 points
def exercise08():
    '''
        Using the below linked documentation from Binance, use websockets to pull and stream back ANY streaming market data
        (like limit order book) using websockets. The stream should be displayed to console. Feel free to import binance python libs.

        Relevant docs
        https://python-binance.readthedocs.io/en/latest/overview.html
        https://python-binance.readthedocs.io/en/latest/websockets.html
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/web-socket-streams.md
    '''
    
    #states secret and public key
    secret_key = 'AhYt4B9YJsH6cVCqUhmxgOpHvvmoXYLaITkYIJZKRvo4HNK03Wu1JxOKfBi3N0a5'
    public_key = 'B9zEhWB5ODpEYcuoBdur2XupW0cqyqsDi1N1S0KWKvJU4NEeVfD9kxgKRtwoMnlg'
    
    #initializes client
    client = Client(public_key,secret_key)
    
    #creates message processor function to handle payload from websocket
    def process_message(msg):
        print(msg)
    
    
    #initializes socket manager
    bm = BinanceSocketManager(client)
    
    #creates connection to fetch Etherium trade data
    conn_key = bm.start_trade_socket('ETHBTC',process_message)
    
    
    #starts socket
    bm.start()
    
    #wait 10 seconds to let data come in
    time.sleep(10)
    
    #stops socket connection
    bm.stop_socket(conn_key)
    
    #closes socket manager
    bm.close()


class TestAssignment7(unittest.TestCase):
    def test_exercise07(self):
        rm, ps = exercise07()
        self.assertEqual(len(rm),50)
        self.assertEqual(len(ps),50)

    def test_exercise06(self):
        ptr = exercise06()
        self.assertTrue(len(ptr),506)

    def test_exercise05(self):
        aa, am, mnpy = exercise05()
        self.assertAlmostEqual(aa,68.57,2)
        self.assertAlmostEqual(am,22.53,2)
        self.assertTrue(len(mnpy),506)
        
    def test_exercise04(self):
         print('Skipping EX4 tests')     

    def test_exercise03(self):
        score = exercise03(8,.25)
        self.assertAlmostEqual(exercise03(8,.3),.955,2)
        self.assertAlmostEqual(exercise03(8,.25),.947,2)
    def test_exercise02(self):
        pred = exercise02([[6.7,3.1,5.6,2.4],[6.4,1.8,5.6,.2],[5.1,3.8,1.5,.3]])
        self.assertTrue('setosa' in pred)
        self.assertTrue('virginica' in pred)
        self.assertTrue('versicolor' in pred)
        self.assertEqual(len(pred),3)
    def test_exercise01(self):
        df, tn = exercise01()
        self.assertEqual(df.shape,(5,4))
        self.assertEqual(df.iloc[0,1],3.5)
        self.assertEqual(df.iloc[2,3],.2)
        self.assertTrue('setosa' in tn)
        self.assertEqual(len(tn),3)
     

if __name__ == '__main__':
    unittest.main()

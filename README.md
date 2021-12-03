# Final Project: Market Research on Product Ratings
In this final project we built 2 models that explores the ratings that each user would give to each product.
In the models we have:

* Load and prepare the "user_ratings.csv" and "user_history.csv" files for analysis
* create a csv file that contains 45000 X 75 lines with 3 columns in the same format as the "user_ratings.csv" and "user_history.csv"

## Model 1: SGD Regressor 

### Step 1: Kmeans clustering/PCA Analysis
First import the folowing packages: 
* sklearn.cluster.Kmeans 
* matplotlib.pyplot 
* numpy 
* pandas
* %matplotlib inline
* import PCA from sklearn.decomposition
* import StandardScaler from sklearn.preprocessing 
* import LinearRegression from sklearn.linear_model 
* import cluster from sklearn 


Then read in and process "user_ratings.csv" and "user_history.csv" using the pandas package "read_csv".

Implement the elbow method for Kmeans clustering to find the appropriate amount of clusters to use on "user_history.csv". Plot the results on a graph to visualize the 'elbow' on each cluster. 


### Step 2: Building the SGD Regressor




## Model 2: Keras Model 

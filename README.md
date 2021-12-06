# Final Project: Market Research on Product Ratings
In this final project we built 2 models that explores the ratings that each user would give to each product.
In the models we have:

* Load and prepare the "user_ratings.csv" and "user_history.csv" files for analysis
* create a csv file that contains 45000 X 75 lines with 3 columns in the same format as the "user_ratings.csv" and "user_history.csv"

## Model 1: SGD Regressor 

### Step 1: Kmeans clustering/PCA Analysis
First import the folowing packages: 
* sklearn
* matplotlib
* numpy 
* pandas
* %matplotlib inline
   
#### Part 1: Kmeans Clustering

Then read in and process "user_ratings.csv" and "user_history.csv" using the pandas package "read_csv".

Using the cluster package in sklearn, implement the elbow method for Kmeans clustering to find the appropriate amount of clusters to use on "user_history.csv". Plot the results on a graph, with plyplot, to visualize the 'elbow' on each cluster. 

#### Part 2: PCA analysis
Using the decomposition package in sklearn change the "user_history.csv" into 2 dimensions and normalizing the data by using the preprocessing package. Then transform the data into pca features with fit_transform.  

Create a plot of the variance of the PCA components using matplotlib plyplot. Find the variance of each of the pca feautres with explained_variance_ratio_ and rounding the values to an appropriate number of decimal places. For each variance create labels to fiquire out the frequency of each variance. 

Using the cluster package in sklearn, make 3 clusters and fit on "user_history.csv".
Then find the centers of each cluster using the model from fitting the history data using the package clsuter_centers_. Create a new model that recreates the 3 clusters with arrays using the Kmeans cluster package. Create a for loop that runs through the unique centers of of the Kmeans model and plot each entity in the user_history data accordingly on a scatter plot. 


### Step 2: Building the SGD Regressor
Using the clusters that were identified in the previous step, create three dataframes: one for each cluster that includes all of the information from "user_history.csv" that are part of the cluster. 

Call the make_pipeline package from sklearn with parameters being StandardScalar and SGDRegressor using the default parameters included in SGDRegressor to create the model. 

For each of the three dataframes created for each cluster, do the following:

 1. Iterate through each of the 75 products included in "user_ratings.csv". 
 2. Index the user_history information to only include users that already have ratings for the products being analyzed (remove any users where the product rating is NA for that product). 
 3. Fit the model on this data and use it to predict ratings for all of the users for that product. Repeat this for all products and for each cluster dataframe.
 4. Add these predictions to a dataframe

Merge the results and using the melt function, transform the data into the appropriate format similar to "user_ratings.csv". This data will be used to compare our predictions to the predictions included in "user_ratings.csv" and calculate the accuracy.



## Model 2: Keras Model 
### Step 1: Setting up
First import the folowing packages: 
* sklearn
* matplotlib
* numpy 
* pandas
* mpl_toolkits.mplot3d
* tensorflow
* keras

### Step 2: Get all Data
Firstly we merged the two csv files into one with shape 4500 * 176. Each row in the merged datafrome represents the attributes for one user. For each user, there are 100 history percentage coefficients and 75 ratings for different products.
Then, the first 3500 users' data are splitted into the training set and the rest are put into the testing set. 
In the end, in order to use the data in the model, we turned these dataframes into numpy arrays with shape 3500*100 and 3500*75 namely the first input and second input.

   
### Step 3: Building the Keras Model
The goal for the Keras model is to find a tranformation matrix W to map the 100 percentage coefficients into an array with length 75. In other words, we want to match the 75 ratings with the given 100 percentage coefficients. This is the model we used:
 1. Fill in 5 to the missing entries.
 2. Apply sigmoid activation function for the middle layer.
 3. Apply softmax activation function for the final output layer.
 4. Apply mean square error loss function to the model.
 5. Train the model for 1000 times.
In the end, the accuracy rate is about 63%.


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


### Step 2: Building the SGD Regressor
Using the clusters that were identified in the previous step, create three dataframes: one for each cluster that includes all of the information from "user_history.csv" that are part of the cluster. 

Call the make_pipeline package from sklearn with parameters being StandardScalar and SGDRegressor using the default parameters included in SGDRegressor to create the model. 

For each of the three dataframes created for each cluster, do the following:
 1.Iterate through each of the 75 products included in "user_ratings.csv". 
 2.Index the user_history information to only include users that already have ratings for the products being analyzed (remove any users where the product rating is NA for that product). 
 3.Fit the model on this data and use it to predict ratings for all of the users for that product. Repeat this for all products and for each cluster dataframe.
 4.Add these predictions to a dataframe

Merge the results and using the melt function, transform the data into the appropriate format similar to "user_ratings.csv". This data will be used to compare our predictions to the predictions included in "user_ratings.csv" and calculate the accuracy.



## Model 2: Keras Model 

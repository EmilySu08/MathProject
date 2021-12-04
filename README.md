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




## Model 2: Keras Model 

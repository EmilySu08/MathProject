# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 19:20:39 2021

@author: armad
"""

# 3 types of users identified, classified by personal preference.
# For each trait of personal preference, finds how browse history relates to ratings
cluster_0_predict=[]
ID=cluster_0['USER ID']
df0=pd.DataFrame(ID)
for i in range(101,176):
    product=products[i-101]
    
    #cluster browse history 
    X=cluster_0.iloc[:,0:101]
    
    #rating on i-th non product
    Y=cluster_0.iloc[:,[0,i]]
    Z=Y[~Y.iloc[:,1].isna()]
    
    #data is cluster 0 history vs.rating of i-st product, only for users with non-na rating
    data=pd.merge(X,Z,how='inner')
    
    #SGD fit between cluster history and i-st product rating, reg looks at how user history affects rating for product i st. 
    feature=data.iloc[:,1:101]
    target=data.iloc[:,-1]
    reg.fit(feature, target)
    
    #Apply model to all users, obtain full rating "prediction" for product i-st.
    features=cluster_0.iloc[:,1:101]
    prediction=reg.predict(features)
    cluster_0_predict.append(prediction)
    df0[product]=prediction
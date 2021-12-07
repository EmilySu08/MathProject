#Please append after KmeansV2 for correct running
from sklearn.metrics import r2_score
user_ratings_table.reset_index(level=0, inplace=True)

rating_test = []
prediction_test = []

user_rating_list = user_ratings_table.values.tolist()
merged_list = merged.values.tolist()



rating_test = user_ratings_table[['USER ID','adrian crater']]

rating_test = pd.DataFrame(rating_test)
rating_test.set_index('USER ID',inplace=True)

prediction_test = merged[['USER ID','adrian crater']]
prediction_test = pd.DataFrame(prediction_test)
prediction_test.set_index('USER ID',inplace=True)

rating_test=rating_test.dropna()



tester=rating_test.merge(prediction_test,on='USER ID',how='inner')


test1 = tester['adrian crater_x']
test2 = tester['adrian crater_y']
r = r2_score(test1, test2)

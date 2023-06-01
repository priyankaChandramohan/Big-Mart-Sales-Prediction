# Big-Mart-Sales-Prediction
The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim is to build a predictive model and find out the sales of each product at a particular store.
Using this model, BigMart will try to understand the properties of products and stores which play a key role in increasing sales.

## Main Goal:
- Create an analytical framework to understand Key factors impacting Sales.
- Develop a modeling framework
- To estimate the stores which play a key role in increasing sales.
 
## Variable Description
- ProductID : unique product ID
- Weight : weight of products
- FatContent : specifies whether the product is low on fat or not
- Visibility : percentage of total display area of all products in a store allocated to the particular product
- ProductType : the category to which the product belongs
- MRP : Maximum Retail Price (listed price) of the products
- OutletID : unique store ID
- EstablishmentYear : year of establishment of the outlets
- OutletSize : the size of the store in terms of ground area covered
- LocationType : the type of city in which the store is located
- OutletType : specifies whether the outlet is just a grocery store or some sort of supermarket
- OutletSales : (target variable) sales of the product in the particular store

## Recommendations:
- Classification algorithms can be used to predict if a house is near a coastal area. 
- Clustering algorithms can be used to identify similar neighbors
- Machine learning algorithms can predict the value of a building or asset over the next decade, based on data from the last few years. You can see exactly how much profit you will get in the next 10 years. !!
- Using machine learning algorithms in recommender systems helps buyers find property details and unique insights of it.

## Final Words:
- We can conclude from above that GridSearchCV is giving better results compared to that of tuning done by graphical method of individual parameters or RandomSearchCV
- The ensemble models have performed well compared to that of linear,KNN,SVR models, logistic
- The best performance is given by Gradient boosting model
- The top key features that drive the price of the property are: 'furnished_1', 'yr_built', 'living_measure','quality_8', 'HouseLandRatio', 'lot_measure15', 'quality_9', 'ceil_measure', 'total_area'
- The above data is also reinforced by the analysis done during bivariate analysis.

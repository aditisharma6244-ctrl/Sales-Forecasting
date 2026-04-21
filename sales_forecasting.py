# Sales Forecasting using Regression and Time-Based Features
This project aims to forecast sales using historical data. 
It includes data cleaning, time-based feature engineering, 
regression modeling, and performance evaluation.

The goal is to generate insights and visualizations that 
can be easily understood by non-technical stakeholders.
  
# Load dataset:
train = pd.read_csv("train.csv")

# Data Understanding:
print(train.head())
print(train.info())
print(train.isnull().sum())

# Feature Engineering:
train['date'] = pd.to_datetime(train['date'])
train['month'] = train['date'].dt.month

# Model Training:
X = train[['store_nbr', 'onpromotion', 'month']]
y = train['sales']

# Model Evaluaion:
print("RMSE:", rmse)
print("R2 Score:", r2_score(y_test, pred))

The model predicts sales using regression techniques. 
The RMSE value indicates the average prediction error, 
while the R² score shows how well the model explains the data.

The results suggest that the model captures general sales trends, 
although some variations remain due to external factors.

The graph compares actual vs predicted sales values. 
The closer the two lines, the better the model performance. 
This visualization helps stakeholders easily understand how accurate the predictions are.
  
# Conclusion:

The project successfully demonstrates a basic sales forecasting model 
using regression and time-based features. 

While the model provides reasonable predictions, further improvements 
can be made by adding more features and using advanced models.

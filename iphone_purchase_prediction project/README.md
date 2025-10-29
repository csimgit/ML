# Classification-Models

## iPhone Purchase Prediction

Iphone Purchases are getting increased day by day and many stores wants to predict whether a customer will purchase an Iphone 
from thier store given their gender, age and salary.

+ Dataset name - iphone_purchases.csv is the raw data and iphone_purchase_cleaned.csv is the processed data for model. Both the dataset are in the data.zip file.

+ Objective  - Whether Customer will purchase or not

+ Tools - Python code in Jupyter notebook, Tableau for vizualization, Powerpoint, Excel.

+ Algorithm Used- KNeighborsClassifier, Decision Tree, Random Forest.

  + KNeighborsClassifier - KNeighborsClassifier is a classification algorithm based on the K-Nearest Neighbors (KNN) approach. 
It is part of the scikit-learn library in Python and is used for solving classification problems. 
KNN is a simple and intuitive algorithm that classifies a new data point based on the majority class of its k-nearest neighbors in the feature space.

  + Decision Tree - A decision tree is a supervised machine learning algorithm used for both classification and regression tasks. 
It works by recursively partitioning the dataset into subsets based on the values of different features. 
The objective is to create a tree-like structure of decisions, where each node represents a decision based on a particular feature, 
and each leaf node represents the predicted outcome.

  + Random Forest - A Random Forest is an ensemble learning method that operates by constructing a multitude of decision trees during training and outputting the class that is the mode of the classes (classification) or the mean prediction (regression) of the individual trees. It is a powerful and versatile machine learning algorithm known for its high accuracy and robustness.

+ Methodology:
  
  •	Data Collection - The data used to build the model was provided in the csv format. It has gender, age, salary and whether the said person purchased the phone or not in 1 and 0 
    format, where 1 stands for yes and 0 for no.

  •	Data Pre-processing - Data pre-processing is a crucial step to ensure the quality and suitability of the dataset for training machine learning models.

  •	Feature Selection - Feature selection is a critical step to identify the most relevant variables that contribute to the predictive power of the model.

  •	Model Selection - In the model selection section, provide a detailed overview of the machine learning algorithms chosen for the predictive analysis. Explain the rationale behind the 
    selection of each algorithm and discuss how they align with the project objectives.
  
  •	Model Training - In the model training section, the processed data is fit to train the selected model so that it is able to predict the future entered data.

  •	Model Evaluation - In the model evaluation section, the performance of the trained machine learning models is assessed to select the best suited model for deployment.

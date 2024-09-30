import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier  # You can replace this with any other classifier you want to use
from sklearn import tree, model_selection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

import numpy as np

# Step 1: Load the CSV dataset with no column names
#data = pd.read_csv('Datasets\zoo.csv', header=None)
#data = pd.read_csv('Datasets\merged_file7.csv', header=None)

dir_in = "output/"
filein = "fin_fin_0101"
file = dir_in + filein
data = pd.read_csv(file, header=None)


# Step 2: Preprocess the data (you may need to handle missing values, encode categorical variables, etc.)

# Step 3: Split the dataset into training and testing sets
X = data.iloc[1:, 1:-1]  # Use all columns except the last one as features
y = data.iloc[1:, -1]   # Use the last column as the target category

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


model = DecisionTreeClassifier()  # You can replace this with any other classifier you want to use
model.fit(X_train, y_train)

# Step 5: Make predictions on the testing data
y_pred = model.predict(X_test)

# Step 6: Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Step 7: Print the accuracy
print(f'Accuracy_1: {accuracy * 100:.2f}%')


run_dt_res = classification_report(y_test, y_pred)

#accuracy = accuracy_score(y_test, y_pred)

# Step 7: Print the accuracy
#print(f'Accuracy: {accuracy * 100:.2f}%')
print("\nReport:")
print(f"{run_dt_res}")

"""
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

clf = RandomForestClassifier(n_jobs=-1)

param_grid = {
    "n_estimators": np.arange(100, 1500, 100),
    "max_depth": np.arange(1, 20),
    "criterion": ["gini", "entropy"],
}

model = model_selection.RandomizedSearchCV(
    estimator=clf,
    param_distributions=param_grid,
    n_iter=7,
    scoring="accuracy",
    verbose=1,
    n_jobs=1,
    cv=4,
)

y_train = y_train.astype('int')
model.fit(X_train, y_train.ravel())  # RandomForestClassifier (clf) encapsulated in RandomizedSearchCV

y_pred = model.predict(X_test)
#label_dict = {0: "non-extinction", 1: "extinction"}
y_test = y_test.astype('int').ravel()

run_dt_res = classification_report(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)

# Step 7: Print the accuracy
print(f'Accuracy: {accuracy * 100:.2f}%')
print("\nReport:")"""
#print(f"{run_dt_res}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier  # You can replace this with any other classifier you want to use

# Step 1: Load the CSV dataset with no column names
#data = pd.read_csv('Datasets\merged_file7.csv', header=None)


data = pd.read_csv('path_to_merged_csv4.csv', header=None)

# Step 2: Preprocess the data (you may need to handle missing values, encode categorical variables, etc.)

# Step 3: Split the dataset into training and testing sets
X = data.iloc[:, 1:-1]  # Use all columns except the last one as features
y = data.iloc[:, -1]   # Use the last column as the target category

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# Step 4: Train a classification model on the training data
model = DecisionTreeClassifier()  # You can replace this with any other classifier you want to use
model.fit(X_train, y_train)

# Step 5: Make predictions on the testing data
y_pred = model.predict(X_test)

# Step 6: Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Step 7: Print the accuracy
print(f'Accuracy: {accuracy * 100:.2f}%')
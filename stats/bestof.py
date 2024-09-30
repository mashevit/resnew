import numpy as np
import pandas as pd
#from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def ml_alg(csv_file):

    data = pd.read_csv(csv_file, header=None)
    # Load the dataset
    #data = load_iris()
    X = data.iloc[1:, 1:-1]  # Use all columns except the last one as features
    y = data.iloc[1:, -1]   # Use the last column as the target category

    #X = data.data
    #y = data.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Apply SelectPercentile
    percentile_selector = SelectPercentile(score_func=f_classif, percentile=50)
    X_train_selected = percentile_selector.fit_transform(X_train, y_train)
    X_test_selected = percentile_selector.transform(X_test)

    # Get the indices of the selected and discarded features
    selected_indices = np.where(percentile_selector.get_support())[0]
    discarded_indices = np.where(~percentile_selector.get_support())[0]

    print(f'Selected indices with SelectPercentile: {selected_indices}')
    print(f'Discarded indices with SelectPercentile: {discarded_indices}')

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_selected, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_selected)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy with SelectPercentile: {accuracy:.4f}')




    # Apply SelectKBest
    kbest_selector = SelectKBest(score_func=f_classif, k=10)
    X_train_selected = kbest_selector.fit_transform(X_train, y_train)
    X_test_selected = kbest_selector.transform(X_test)

    # Get the indices of the selected and discarded features
    selected_indices = np.where(kbest_selector.get_support())[0]
    discarded_indices = np.where(~kbest_selector.get_support())[0]

    print(f'Selected indices with SelectKBest: {selected_indices}')
    print(f'Discarded indices with SelectKBest: {discarded_indices}')

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_selected, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_selected)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy with SelectKBest: {accuracy:.4f}')


ml_alg("../zoo1/zoo15.data")
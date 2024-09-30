import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier  # You can replace this with any other classifier you want to use
from sklearn import tree, model_selection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

import numpy as np


def ml_alg(csv_file):

    data = pd.read_csv(csv_file, header=None)
    rr = 4
    flag = False
    # Step 2: Preprocess the data (you may need to handle missing values, encode categorical variables, etc.)

    # Step 3: Split the dataset into training and testing sets
    X = data.iloc[1:, 1:-1]  # Use all columns except the last one as features
    y = data.iloc[1:, -1]   # Use the last column as the target category

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rr)






    print("with original")
    #data = pd.read_csv("../zoo2/zoo2.data", header=None)
    rr = 42
    flag = False
    # Step 2: Preprocess the data (you may need to handle missing values, encode categorical variables, etc.)

    # Step 3: Split the dataset into training and testing sets
    X = data.iloc[1:, 1:-1]  # Use all columns except the last one as features
    y = data.iloc[1:, -1]   # Use the last column as the target category


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rr)

    # Train a RandomForestClassifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy52:", accuracy)

    print("Accuracy5:2", accuracy * 100, "%")



    data = pd.read_csv(csv_file, header=None)
    rr = 42
    flag = False
    # Step 2: Preprocess the data (you may need to handle missing values, encode categorical variables, etc.)

    # Step 3: Split the dataset into training and testing sets
    X = data.iloc[1:, 1:-1]  # Use all columns except the last one as features
    y = data.iloc[1:, -1]   # Use the last column as the target category

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rr)



    model = DecisionTreeClassifier()  # You can replace this with any other classifier you want to use
    model.fit(X_train, y_train)

    # Step 5: Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Step 6: Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)

    # Step 7: Print the accuracy
    print(f'Accuracy_12: {accuracy * 100:.2f}%')
    run_dt_res = classification_report(y_test, y_pred)
    print("\nReport2:")
    print(f"{run_dt_res}")


    clf = DecisionTreeClassifier()
    selector = SelectFromModel(clf)
    X_new = selector.fit_transform(X, y)


    selected_features = selector.get_support()
    selected_feature_names = X.columns[selected_features]
    X_selected = X[selected_feature_names]
    #X_selected = X[:, selected_features]
    selected_feature_indices = np.where(selected_features)[0]
    left_out_feature_indices = np.where(~selected_features)[0]

    print({f"13 {X_selected}"})

    print({f"13 {selected_feature_indices}"})

    print({f"13 {left_out_feature_indices}"})



    X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=rr)


    model = DecisionTreeClassifier()  # You can replace this with any other classifier you want to use
    model.fit(X_train, y_train)

    # Step 5: Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Step 6: Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)

    # Step 7: Print the accuracy
    print(f'Accuracy_14: {accuracy * 100:.2f}%')
    run_dt_res = classification_report(y_test, y_pred)
    print("\nReport4:")
    print(f"{run_dt_res}")




    # clf = RandomForestClassifier()
    # selector = SelectFromModel(clf)
    # X_new = selector.fit_transform(X, y)
    '''

    clf = RandomForestClassifier()
    selector = SelectFromModel(clf)
    X_new = selector.fit_transform(X, y)


    selected_features = selector.get_support()
    selected_feature_names = X.columns[selected_features]
    X_selected = X[selected_feature_names]
    #X_selected = X[:, selected_features]
    selected_feature_indices = np.where(selected_features)[0]
    left_out_feature_indices = np.where(~selected_features)[0]

   # print({f"15 {X_selected}"})

    print({f"15 {selected_feature_indices}"})

    print({f"15 {left_out_feature_indices}"})


    # Assuming X is your feature matrix and y is your target variable

    # Step 1: Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=42)

    # Step 2: Use SelectFromModel to select features
    clf = RandomForestClassifier()
    selector = SelectFromModel(clf)
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)

    # Step 3: Train the classifier on the selected features
    clf.fit(X_train_selected, y_train)
    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy5:3", accuracy)

    print("Accuracy5:3", accuracy * 100, "%")

    # Step 4: Evaluate the classifier on the testing set
    accuracy = clf.score(X_test_selected, y_test)
    print(f"Accuracy: {accuracy}")
    '''


    '''
    clf = RandomForestClassifier(random_state=rr)

    # Perform feature selection
    selector = SelectFromModel(clf)
    X_train_new = selector.fit_transform(X_train, y_train)

    # Transform the test set using the same selector
    X_test_new = selector.transform(X_test)

    # Get the selected feature indices and names
    selected_features = selector.get_support()
    selected_feature_names = X.columns[selected_features]
    selected_feature_indices = np.where(selected_features)[0]
    left_out_feature_indices = np.where(~selected_features)[0]

    # Train the model using the selected features
    clf.fit(X_train_new, y_train)

    # Evaluate the model
    y_pred = clf.predict(X_test_new)
    accuracy = accuracy_score(y_test, y_pred)

    print(f'Accuracy with selected features: {accuracy:.4f}')
    print(f'Selected feature names: {selected_feature_names}')
    print(f'Selected feature indices: {selected_feature_indices}')
    print(f'Left-out feature indices: {left_out_feature_indices}')
    '''




    # Initialize the RandomForestClassifier
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rr)
    clf = RandomForestClassifier(random_state=42)

    # Perform feature selection
    selector = SelectFromModel(clf)
    X_train_new = selector.fit_transform(X_train, y_train)

    # Transform the test set using the same selector
    X_test_new = selector.transform(X_test)

    # Get the selected feature indices and names
    selected_features = selector.get_support()

    # Ensure the boolean mask is the same length as the number of columns in X
    assert selected_features.shape[0] == X.shape[1], "Mismatch in number of columns and selected features"

    selected_feature_names = X.columns[selected_features]
    selected_feature_indices = np.where(selected_features)[0]
    left_out_feature_indices = np.where(~selected_features)[0]

    print("Selected feature names:", selected_feature_names)
    print("Selected feature indices:", selected_feature_indices)
    print("Left-out feature indices:", left_out_feature_indices)

    # Train the model using the selected features
    clf.fit(X_train_new, y_train)

    # Evaluate the model
    y_pred = clf.predict(X_test_new)
    accuracy = accuracy_score(y_test, y_pred)

    print(f'Accuracy with selected features: {accuracy:.4f}')

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rr)

    # Train a RandomForestClassifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy5:", accuracy)

    print("Accuracy5:", accuracy * 100, "%")



    print("with original")
    #data = pd.read_csv("../zoo2/zoo2.data", header=None)
    rr = 42
    flag = False
    # Step 2: Preprocess the data (you may need to handle missing values, encode categorical variables, etc.)

    # Step 3: Split the dataset into training and testing sets
    X = data.iloc[1:, 1:-1]  # Use all columns except the last one as features
    y = data.iloc[1:, -1]   # Use the last column as the target category


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rr)

    # Train a RandomForestClassifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Make predictions
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy52:", accuracy)

    print("Accuracy5:2", accuracy * 100, "%")




    if flag:
        X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=rr)


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
        print("\nReport:")
        print(f"{run_dt_res}")




        X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=rr)


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
        print("\nReport:")
        print(f"{run_dt_res}")





print('a')

ml_alg("../zoo2/zoo25.data")
print('b')
ml_alg("../zoo2/zoo2.data")
print('c')

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
    print("\nReport:")
    print(f"{run_dt_res}") """

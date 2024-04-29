from sklearn.preprocessing import OrdinalEncoder
from feature_selection import feature_selection_decision_tree
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


def decision_tree(df, df2, features):
    print("\n===Decision Tree===")
    y = OrdinalEncoder().fit_transform(df[['minions_killed']])
    y_test = OrdinalEncoder().fit_transform(df2[['minions_killed']])
    X_train = df[features]
    X_test = df2[features]

    dt = DecisionTreeClassifier(criterion='entropy')
    ohe = OneHotEncoder()
    ohe.fit(X_train)
    X_train_ohe = ohe.transform(X_train).toarray()

    dt.fit(X_train_ohe, y)

    X_test_ohe = ohe.transform(X_test)
    y_pred = dt.predict(X_test_ohe)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


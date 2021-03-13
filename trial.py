import pandas as pd
from tabulate import tabulate as tb
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing

### source = https://www.datacamp.com/community/tutorials/decision-tree-classification-python

# CSV FILE #

with open(r"C:\Users\Student\Documents\Uni\Year 2\Team Software Engineering (CMP2804M)\Assessment 3\Machine Learning tries\music.csv") as f:

    data = pd.read_csv(f, header=0, encoding="utf-8-sig", engine="python")

data.columns = [x.encode("utf-8").decode("ascii", "ignore") for x in data.columns]

features = ['tempo', 'tombre', 'length', 'target'] #etc.

print(tb(data, headers=features))
print()

# SPLITE DATA INTO TESTING AND TRAINING DATA #

X = data[features]

Y = data.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

print("X_test: ", X_test)
#print("X_train:", X_train)
#print("Y_test:", Y_test)
#print("Y_train:", Y_train)

# MACHINE LEARNING #

clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)

clf = clf.fit(X_train, Y_train)

y_pred = clf.predict(X_test) 
print(y_pred)

print("Accuracy:", metrics.accuracy_score(Y_test, y_pred))

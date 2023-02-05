"""
Train the model based on iris dataset
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pickle

# load data
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)
# save the model
pickle.dump(model, open("model.pkl", "wb"))

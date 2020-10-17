from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import CategoricalNB

# classifiers is a list of classifier classes
# the fist one is the final classifier
# all other classifiers feed to final classifier
classifiers = [RandomForestClassifier,
               SGDClassifier, SVC]

# classifier_parameters is a list dictionaries
# each dictionary contains listed parameters for classifiers
# {parameter1:[value1,value2...], ...}
# this means len(classifiers) must be equal to len(classifiers_parameters)
classifiers_parameters = [{'max_depth': [2, 5],
                           'max_leaf_nodes': [2, 10],
                           'max_samples': [10, 20, None]},
                          {'penalty': ['l2']},
                          {'kernel': ['linear', 'rbf'], 'C':[1, 0.1]}]

Engine = (classifiers, classifiers_parameters)

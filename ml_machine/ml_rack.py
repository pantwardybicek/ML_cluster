
from ml_machine import report
import numpy as np


class Rack ():
    def __init__(self, machine):
        self.M = machine

    def accept_classifiers (self, classifiers):
        self.final_classifier = classifiers[0]
        self.base_classifiers = [x for x in classifiers[1:]]
        report({'estimators':{'estimators_base': ','.join([c.__name__ for c in self.base_classifiers]),
               'estimators_final': self.final_classifier.__name__,
               'rack_status': 'accepted classifiers'}})

    def deploy (self, rack_parameters: list):
        final_parameters = rack_parameters[0]
        report({'parameters:':{'estimators_params_base': rack_parameters[1:],
                'estimators_params_final': rack_parameters[0]}})
        self.final_rack = [self.deploy_estimator(self.final_classifier, **final_parameters)]
        base_parameters = rack_parameters[1:]
        self.base_rack = [
            self.deploy_estimator(c, **p) for (c,p) in tuple(zip((c for c in self.base_classifiers),
                                                                  (p for p in base_parameters)))
        ]

    def deploy_estimator (self, classifier, **kwargs):
        return classifier(**kwargs)

    def base_fit(self,X, y):
        if self.M.setup['baserack_trainset_split'] == False:
            report({'rack_status': 'fitting base estimators - all trainset in each'})
            self.base_rack_fitted = [classifier.fit(X,y) for classifier in self.base_rack]
        elif type(self.M.setup['baserack_trainset_split']) == tuple:
            report({'rack_status': 'fitting base estimators - trainset split'})
            split_X = [X[:,a:b] for (a,b) in self.M.setup['baserack_trainset_split']]
            self.base_rack_fitted = [pair[0].fit(pair[1], y) for pair in zip(self.base_rack, split_X)]


    def base_predict(self,X):
        report({'rack_status': 'base_rack predicting'})
        n_base_estimators = len(self.base_rack_fitted)
        if self.M.setup['baserack_trainset_split'] == False:
            return np.array([estimator.predict(X) for estimator in self.base_rack_fitted]).reshape(-1,n_base_estimators)
        elif type(self.M.setup['baserack_trainset_split']) == tuple:
            report({'rack_status': 'fitting base estimators - trainset split'})
            split_X = [X[:, a:b] for (a, b) in self.M.setup['baserack_trainset_split']]
            return np.array([pair[0].predict(pair[1]) for pair in zip(self.base_rack_fitted, split_X)]).reshape(-1,n_base_estimators)

    def final_fit(self,X,y):
        report({'rack_status': 'fitting final estimator'})
        self.final_rack_fitted = [self.final_rack[0].fit(X,y)]

    def final_predict(self,X):
        report({'rack_status': 'final_rack predicting'})
        return self.final_rack_fitted[0].predict(X)


    def clear (self):
        report({'rack_status': 'cleared'})
        self.final_rack = []
        self.base_rack =[]

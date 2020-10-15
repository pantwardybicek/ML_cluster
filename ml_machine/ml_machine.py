import os
import requests


def report(params: dict):
    api_url = 'http://api:8000/' + str(os.environ['machine_number'])
    requests.post(api_url, json=params)

from ml_engine import Engine
from ml_rack import Rack
from ml_turntable import Turntable
from ml_preprocess import Preprocess
from ml_work import Work
from ml_setup import Setup


from threading import Thread
import numpy as np


m=False #provides a variable for machine_api



class Machine (Thread):
    def __init__ (self, engine, setup, data):
        self.classifiers = engine[0]
        self.classifiers_parameters = engine[1]
        self.data =list()
        self.trained_estiamtors = list()
        self.engine = engine
        self.setup = setup
        self.data = data
        super().__init__()
        global m
        m = True


    def run (self):
        self.learn()
        return message

    def learn(self):
        report({'machine_status': 'preparing'})
        self.R = Rack(self)
        self.R.accept_classifiers(self.engine[0])
        self.T = Turntable(self.engine[1])
        self.Pre = Preprocess(self, self.data)
        X, y = self.Pre.train()
        report({'turntable_length': len(self.T.turntable)})
        self.W = Work(self, X, y)
        report({'metrics': self.W.metrics})
        report({'machine_status': 'job_completed',
                'metrics':self.W.metrics})



def main ():
    data = [np.load('/var/ml_data/' + x, allow_pickle=True) for x in os.listdir('/var/ml_data') if x[-3:] == 'npy']
    machine_number = os.environ['machine_number']
    report({'machine_number': machine_number})
    M = Machine(Engine, Setup, data)
    report({'machine_status': 'instantiated'})
    M.start()
    message = 'Machine '+os.environ['machine_number']+' started successfully'
    return message





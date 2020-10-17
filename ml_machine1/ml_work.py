from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
from ml_machine import report, report_metrics

class Work():
    def __init__ (self, machine, X, y):
        report({'rack_status': 'tasks applied',
                'machine_status': 'working'})
        self.M = machine
        self.R = self.M.R
        self.turntable = self.M.T.turntable
        self.metrics = list()
        turn_no = 1
        for turn_params in self.turntable:
            report({'current_turn': turn_no})
            self.turn(turn_no, turn_params, X, y)
            turn_no += 1


    def turn(self,turn_no, turn_params, X, y):
        self.R.deploy(turn_params)
        report({'machine_status':'fitting base rack'})
        self.R.base_fit(X, y)
        base_result = self.R.base_predict(X)
        report({'machine_status': 'fitting final rack'})
        self.R.final_fit(base_result, y)
        report({'machine_status': 'final rack predicting'})
        self.result = self.R.final_predict(base_result)
        report({'machine_status': 'performing metrics calculation'})
        self.metrics.append(self.count_efficacy(turn_no, turn_params, y))


    def count_efficacy(self,turn_no, turn_params, true_y):
        acc_sc = accuracy_score(true_y, self.result)
        prec_sc = precision_score(true_y, self.result)
        f1_sc = f1_score(true_y, self.result)
        recall_sc = recall_score(true_y, self.result)
        metrics = {'turn_no': str(turn_no),
                   'machine_id':self.M.id,
                   'turn_params': str(turn_params),
                   'accuracy_score': acc_sc,
                   'precision_score': prec_sc,
                   'recall_score': recall_sc,
                   'f1': f1_sc
                   }
        report_metrics(metrics)
        return metrics

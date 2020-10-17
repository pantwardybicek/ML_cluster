from flask import Flask, request, render_template
import json
import app_logic

report_path = '/var/ml_data/cluster_report.txt'

app = Flask(__name__)
'''
get.app/all
get.app/cluster
get.app/1
post.app/1[json ={params}  #updates report: cluster with container params [creates container if not in cluster]
post.app/1 # removes all data about container'''

@app.route('/', methods = ['GET'])
def indeks():
    return app_logic.get_logic('all', request)

@app.route('/table/<container>', methods=['GET'])
def tables(container=None):
    return app_logic.get_table(container)

@app.route('/<container>', methods=['GET', 'POST'])
def sub(container=None):
    if request.method == 'GET':
        return app_logic.get_logic(container, request)

    elif request.method == 'POST':
        params = request.json
        return app_logic.post_logic(container, params)

    else:
        return "HTTP METHOD NOT ACCEPTED"

if __name__ == '__main__':
    with open(report_path, 'w', encoding='ASCII') as file:
        file.write('{"cluster":{}}')
    app.run(host='0.0.0.0', port = 8000)


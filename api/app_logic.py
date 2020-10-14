import json
import requests
from flask import render_template


def update_container_report(container, container_params):
    with open('cluster_report.txt', 'r', encoding='utf-8') as file:
        all = json.loads(file.read())
        if len(all) == 0:
            all = {'cluster': dict()}
        cluster = all['cluster']
    with open('cluster_report.txt', 'w', encoding='utf-8') as file:
        if container in cluster:
            if len(container_params) > 0:
                cluster[container].update(container_params)
            else:
                cluster.update({container: dict()})
        else:
            if len(container_params) > 0:
                cluster.update({container: container_params})
            else:
                cluster.update({container: dict()})

        file.write(json.dumps(all))
        return json.dumps(cluster[container], indent=4)


def get_logic(container, request):
    if request.method == 'GET':
        return get_report(container)


def get_report(container):
    with open('cluster_report.txt', 'r', encoding='ASCII') as file:
        j = json.loads(file.read())
        if container == 'all':
            return render_template('cluster.html', cluster=json.dumps(j, indent=3, sort_keys=True, separators=(", ", " : ")))
        if 'cluster' in j:
            if container == 'cluster':
                return template_segmented(j['cluster'])
            elif container.isdigit():
                if container in j['cluster']:
                    return template_segmented(j['cluster'][str(container)])
                else:
                    return template_plain('NO CONTAINER:' + container)
            elif container[-3:] == 'run':
                run_containered_machine(container[:-3])
                return template_plain('RUN request has been sent to the machine :' + container[:-3])

            elif container[-7:] == 'machine':
                return template_plain(get_machine_response(container[:-7]))
        else:
            return template_plain('NO CLUSTER WORKING')


def template_segmented(Json):
    sorted_keys = list(Json.keys())
    sorted_keys.sort()
    jlist = {json.dumps({key:Json[key]}, indent=3, sort_keys=True, separators=(", ", " : ")) for key in sorted_keys}
    return render_template('segmented.html', jlist=jlist)

def template_plain(tekst):
    return render_template('plain.html', tekst=tekst)



def post_logic(container, params: json):
    log_post(container, params)
    if container.isdigit():
        return update_container_report(container, params)
    else:
        return "NO CONTAINER INDICATED"


def run_containered_machine(machine_number):
    url = ''.join(('http://machine', machine_number, ':8000/run'))
    response = requests.get(url)
    return response.content

def get_machine_response(machine_number):
    url = ''.join(('http://machine', machine_number, ':8000'))
    response = requests.get(url)
    print(response.content)
    return response.content.decode('utf-8')

def log_post(container, params: json):
    with open('cluster_log.txt', 'a', encoding='utf-8') as file:
        file.write(json.dumps(params))

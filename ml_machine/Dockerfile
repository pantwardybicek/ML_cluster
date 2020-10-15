FROM 'python:3.8.6-buster'
WORKDIR /ml_machine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["mkdir /var/ml_data"]
CMD ["python", "machine_api.py", ">", "/var/ml_data/machine1.out"]
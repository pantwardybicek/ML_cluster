FROM 'python:3.8.6-buster'
WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY api.py api.py
COPY app_logic.py app_logic.py
COPY ./templates ./templates
COPY ./static ./static
EXPOSE 8008
CMD ["mkdir /var/ml_data"]
CMD ["python", "api.py", ">", "/var/ml_data/api.out"]
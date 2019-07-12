FROM python:3.6

COPY . /server

WORKDIR /server

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT  ["python", "-u", "server.py"]

FROM python:3.7.7-slim

RUN apt-get update -y
RUN apt-get install -y locales locales-all
RUN pip3 install flask_pymongo flask


COPY . /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]

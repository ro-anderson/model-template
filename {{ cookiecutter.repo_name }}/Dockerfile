FROM python:3.7-alpine3.7

RUN pip3 install --upgrade pip

RUN mkdir /{{cookiecutter.description}}
ADD . /{{cookiecutter.description}}
WORKDIR /{{cookiecutter.description}}

RUN pip3 install -r requirements.txt



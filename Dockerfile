#pull base image
FROM python:3.8.5


#set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

#install dependencies
COPY Pipfile.lock /code/
RUN pip install pipenv 
RUN pipenv install --skip-lock --system --dev --keep-outdated

#copy project

COPY . /code/
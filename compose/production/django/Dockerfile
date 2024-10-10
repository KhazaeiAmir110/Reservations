FROM python:3.10

WORKDIR /project

ADD ../../.. /project/

RUN pip install -U pip
RUN pip install pipenv
RUN pipenv install --ignore-pipfile


EXPOSE 8080

CMD ["../scripts/run.sh"]

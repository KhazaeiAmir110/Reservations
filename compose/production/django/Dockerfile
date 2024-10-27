FROM python:3.10

WORKDIR /project

ADD ../../.. /project/

RUN pip install -U pip
RUN pip install pipenv
RUN pipenv install --ignore-pipfile
RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["../scripts/run.sh"]

ENV PATH="/scripts:/py/bin:$PATH"
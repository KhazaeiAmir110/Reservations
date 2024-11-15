FROM python:3.10-slim-bullseye


RUN apt-get update
RUN pip install --no-cache-dir -U pip

WORKDIR /project
COPY . /project/
COPY ./scripts /scripts

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8080

ENV PATH="/scripts:/py/bin:$PATH"

RUN chmod +x /project/scripts/run.sh
CMD ["/project/scripts/run.sh"]

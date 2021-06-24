FROM python:3

RUN apt-get update
RUN pip install flask pandas numpy regex fuzzywuzzy matplotlib datetime sqlalchemy

COPY ./api /api

CMD [ "python", "/api/api.py"]
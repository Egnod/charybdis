FROM python:3.7.4-buster
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip3 install poetry gunicorn
RUN python3 -m poetry install
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8000", "--reload", "charybdis.run:app"]

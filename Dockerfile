FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/stripe_payment

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/stripe_payment